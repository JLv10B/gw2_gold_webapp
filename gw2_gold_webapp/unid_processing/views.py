from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Max
from rest_framework import generics, viewsets
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import api_view
from .models import CustomUser, User_Salvage_Records, User_Outcome_Data
from .serializer import CustomUser_Serializer, User_Salvage_Record_Serializer, User_Outcome_data_Serializer
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
import requests
import json
import os.path
from datetime import datetime
# Create your views here.

class CustomUser_List_ViewSet(generics.ListAPIView):
    """
    This view allows admin to viewa list of all users.
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUser_Serializer

@api_view(['GET'])
def GET_User_Raw_Data_View(request):
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
            # TODO: Is there a better way to handle materials that have value = 0?
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
            new_record_number = User_Salvage_Records.objects.filter(user = request.user).aggregate(largest_record =Max('record_number'))['largest_record'] + 1
        except:
            new_record_number = 1
               
        try:
            os.mkdir(f'test_data/{request.user}/{new_record_number}')
        except:
            print('directory already created')
    
        if os.path.isfile(f'test_data/{request.user}/{new_record_number}/initial_record'):
            file_name = 'final_record' # Wirtes/Rewrites final_record if initial_record has been created
        else:
            file_name = 'initial_record'

        f=open(f"test_data/{request.user}/{new_record_number}/{file_name}", 'w')
        f.write(json.dumps(account_item_dict))
        f.close()

        response = HttpResponse(json.dumps(account_item_dict))

        return response

@api_view(['POST'])
def POST_User_Salvage_Outcome_Data_View(request):
    """    
    This view retrieves JSON object from /test_data/<username>/<record_number>/{Initial_recording|Final_recording}.json and creates a new user_salvage_record object and user_outcome_data object. The record number is automatically determined from the User_salvage_record model. The salvaged_item_id is determined by which unid had the largest difference in count. 

    req:
    username
    record_number
    initial/final_recording

    -Open both initial and final records and extract JSON objects.
    -Calculate the difference for the values in final_recording and initial_recording.
    -Create user_salvage_record object
    -Create user_outcome_data object

    user_salvage_record object:
    -record_number
    -user
    -salvage_date
    -salvaged_item_id: {85016|84731|83008}
    -salvaged_item_count

    user_outcome_data object:
    -record_number
    -gained_item_id
    -gained_item_count
    """

    if request.method == "POST":
        try:
            new_record_number = User_Salvage_Records.objects.filter(user = request.user).aggregate(largest_record =Max('record_number'))['largest_record'] + 1
        except:
            new_record_number = 1

        initial_record = open(f'C:/Users/james/Documents/Coding/gw2_gold_webapp/gw2_gold_webapp/test_data/{request.user}/{new_record_number}/initial_record', 'r')
        initial_record_json = initial_record.read()
        initial_record_dict = json.loads(initial_record_json)

        final_record = open(f'C:/Users/james/Documents/Coding/gw2_gold_webapp/gw2_gold_webapp/test_data/{request.user}/{new_record_number}/final_record', 'r')
        final_record_json = final_record.read()
        final_record_dict = json.loads(final_record_json)

        salvage_item_count = 0

        if '85016' in initial_record_dict:
            if '85016' in final_record_dict:
                initial_record_dict['85016'] = abs(initial_record_dict['85016'] - final_record_dict['85016'])
                del final_record_dict['85016']
            salvage_item_count = initial_record_dict.pop('85016')
            salvage_item_id = '85016'  

        if '84731' in initial_record_dict:
            if '84731' in final_record_dict:
                initial_record_dict['84731'] = abs(initial_record_dict['84731'] - final_record_dict['84731'])
                del final_record_dict['84731']
            if initial_record_dict['84731'] > salvage_item_count:
                salvage_item_count =  initial_record_dict.pop('84731')
                salvage_item_id = '84731'
            else:
                del initial_record_dict['84731']
        
        if '83008' in initial_record_dict:
            if '83008' in final_record_dict:
                initial_record_dict['83008'] = abs(initial_record_dict['83008'] - final_record_dict['83008'])
                del final_record_dict['83008']
            if initial_record_dict['83008'] > salvage_item_count:
                salvage_item_count = initial_record_dict.pop('83008')
                salvage_item_id = '83008'
            else:
                del initial_record_dict['83008']

        User_Salvage_Records.objects.create(
            record_number = new_record_number,
            user = CustomUser.objects.get(username = request.user),
            salvaged_date = datetime.now(),
            salvaged_item_id = salvage_item_id,
            salvaged_item_count = salvage_item_count,
        )

        for gained_item in final_record_dict:
            if gained_item in initial_record_dict:
                final_record_dict[gained_item] = abs(final_record_dict[gained_item] - initial_record_dict[gained_item])
            if final_record_dict[gained_item] == 0:
                pass
            else:
                User_Outcome_Data.objects.create(
                    record_number = User_Salvage_Records.objects.get(record_number = new_record_number),
                    gained_item_id = gained_item,
                    gained_item_count = final_record_dict[gained_item],
                )
                
        return HttpResponse({'Salvage record and outcome data created'})
    
@api_view(['POST'])
def Manual_User_Salvage_Outcome_Data_View(request):
    """
    This function allows a user to manual submit data to create a new user_salvage_record object and user_outcome_data object. The record number is automatically determined from the User_salvage_record model. The salvaged_item_id is determined by which unid had the largest difference in count. 
    
    """
    if request.method == "POST":
        try:
            new_record_number = User_Salvage_Records.objects.filter(user = request.user).aggregate(largest_record =Max('record_number'))['largest_record'] + 1
        except:
            new_record_number = 1

        data = request.data['items']
        manual_record = json.loads(data)
        salvage_item_count = 0
        if '85016' in manual_record:
            salvage_item_count = manual_record.pop('85016')
            salvage_item_id = '85016'  

        if '84731' in manual_record and manual_record['84731'] > salvage_item_count:
            salvage_item_count =  manual_record.pop('84731')
            salvage_item_id = '84731'

        if '83008' in manual_record and manual_record['83008'] > salvage_item_count:
            salvage_item_count = manual_record.pop('83008')
            salvage_item_id = '83008'

        User_Salvage_Records.objects.create(
            record_number = new_record_number,
            user = CustomUser.objects.get(username = request.user),
            salvaged_date = datetime.now(),
            salvaged_item_id = salvage_item_id,
            salvaged_item_count = salvage_item_count,
        )

        for gained_item in manual_record:
            User_Outcome_Data.objects.create(
                record_number = User_Salvage_Records.objects.get(record_number = new_record_number),
                gained_item_id = gained_item,
                gained_item_count = manual_record[gained_item],
            )
                
        return HttpResponse({'Salvage record and outcome data created'})

class User_Salvage_Record_ViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = User_Salvage_Record_Serializer

    def get_queryset(self):
        user = self.request.user
        queryset = User_Salvage_Records.objects.filter(user=user)
        return queryset

class User_Outcome_Data_ViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = User_Outcome_data_Serializer

    def get_queryset(self):
        user = self.request.user.id
        record_number = self.request.data['record_number']
        queryset = User_Outcome_Data.objects.filter(record_number__user = user).filter(record_number = record_number)
        return queryset

@api_view(['POST'])
def POST_User_Salvage_Rate_View(request):
    """
    This function updates user_salvage_rates for the user. This function should be used after a new record is created or after a record is deleted.+
    
    """