from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from rest_framework import generics, viewsets
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import api_view
from .models import CustomUser, User_Salvage_Records
from .serializer import CustomUser_Serializer
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
import requests
import json
import os.path
# Create your views here.

class CustomUser_List_ViewSet(generics.ListAPIView):
    """
    This view allows admin to viewa list of all users.
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUser_Serializer

@api_view(['GET'])
def Pull_User_Raw_Data_View(request):
    """
    This view performs API calls to GW2 Bank, Character inventories, Shared inventory, Materials, Wallet APIs to retrieve current items, returns dictionary {item_id:quantity}. Saves data in local files for developement purposes only. Future data storage will be in S3 or other noSQL database.

    char_inventory:
    [
      {'bags': 
           [
              {'inventory': 
                 [
                    {'id':1234,
                     'count: 1,
                    },
                 ]  
               },
              {'inventory': 
                 [
                    {'id':4321,
                     'count: 2,
                    },
                 ]  
               },
                
            ]
       }
    ]

    bank_items/shared inventory/materials/wallet:
    [
      {
        "id": 123,
        "count": 1,
        ...
      },
      {
        "id": 122,
        "count": 1,
        ...
      },
      ...
    ]
    """
    if request.method == "GET":
        user_api = request.user.api_key
        account_item_dict = {}

        # TODO: Can we optimize pulling data from GW2 API to decrease runtime?

        char_list = requests.get(f'https://api.guildwars2.com/v2/characters/?access_token={user_api}').json()
        for char in char_list:
            char_inventory = requests.get(f'https://api.guildwars2.com/v2/characters/{char}/inventory?access_token={user_api}').json() 
            bag_list = char_inventory['bags']
            for bag_slot in bag_list:
                if bag_slot != None:
                    bag_contents = bag_slot['inventory']
                    for item_slot in bag_contents:
                        if item_slot != None:
                            item_id = item_slot['id']
                            item_count = item_slot['count']
                        if item_id in account_item_dict:
                            account_item_dict[item_id] += item_count
                        else:
                            account_item_dict[item_id] = item_count

        bank_items =  requests.get(f'https://api.guildwars2.com/v2/account/inventory?access_token={user_api}').json() 
        for item_slot in bank_items:
            if item_slot != None:
                item_id = item_slot['id']
                item_count = item_slot['count']
            if item_id in account_item_dict:
                account_item_dict[item_id] += item_count
            else:
                account_item_dict[item_id] = item_count

        shared_inventory_items = requests.get(f'https://api.guildwars2.com/v2/account/bank?access_token={user_api}').json() 
        for item_slot in shared_inventory_items:
            if item_slot != None:
                item_id = item_slot['id']
                item_count = item_slot['count']
            if item_id in account_item_dict:
                account_item_dict[item_id] += item_count
            else:
                account_item_dict[item_id] = item_count

        materials = requests.get(f'https://api.guildwars2.com/v2/account/materials?access_token={user_api}').json()
        for item_slot in materials:
            if item_slot != None:
                item_id = item_slot['id']
                item_count = item_slot['count']
            # TODO: Find a better way to handle materials that have value = 0
            if item_count != 0:
                if item_id in account_item_dict:
                    account_item_dict[item_id] += item_count
                else:
                    account_item_dict[item_id] = item_count 

        wallet = requests.get(f'https://api.guildwars2.com/v2/account/wallet?access_token={user_api}').json()
        coins = wallet[0]
        coins_value = coins['value']
        if 'coin' in account_item_dict:
            account_item_dict['coin'] += coins_value
        else:
            account_item_dict['coin'] = coins_value  

        try:
            new_record_number = User_Salvage_Records.objects.get(user = request.user).record_number + 1
        except:
            new_record_number = 1

        # TODO: Need to check if this actually checks if the correct file exists
        if os.path.isfile(f'{request.user}/{new_record_number}/initial_record.json'):
            file_name = 'final_record'
        else:
            file_name = 'initial_record'

        # TODO: Need to change where the path saves to and creates new dir as needed
        response = HttpResponse(content_type='application/json')  
        response['Content-Disposition'] = f'attachment; filename="{request.user}/{new_record_number}/{file_name}.json"'

        response.write(json.dumps(account_item_dict))

        return response


def Create_User_Salvage_Record_and_Outcome_Data_View(request, initial_record, final_record = None):
    """
    This view creates a new User_salvage_record object and User_outcome_data object with the input data. If the final_record data is None then the User_salvage_record object and User_outcome_data objects will be created from just the initial_record data.

    """
    pass
