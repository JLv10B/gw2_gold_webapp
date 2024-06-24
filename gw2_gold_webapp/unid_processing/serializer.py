from rest_framework import serializers
from .models import GW2_Crafting_Recipes, GW2_Items, GW2_Trading_Post_Data, CustomUser, User_Salvage_Rates, User_Shared_Inventory_Data, User_Inventory_Data, User_Bank_Data, User_Materials_Data,User_Wallet_Data, User_Salvage_Records, User_Outcome_Data
from django.contrib.auth.models import User, Group

class GW2_Recipes_Serializer(serializers.ModelSerializer):
    class Meta:
        model = GW2_Crafting_Recipes
        fields = ['recipe_id', 'output_id_id', 'output_item_count', 'ingredients']

class GW2_Trading_Post_Data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = GW2_Trading_Post_Data
        fields = ['item_id', 'buys', 'sells']

class GW2_Items_Serializer(serializers.ModelSerializer):
    class Meta:
        model = GW2_Items
        fields = ['item_id', 'item_name', 'type', 'rarity', 'vender_value']

class CustomUser_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
