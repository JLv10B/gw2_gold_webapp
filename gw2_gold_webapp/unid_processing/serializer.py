from rest_framework import serializers
from .models import GW2_Items, GW2_Recipes, GW2_Trading_Post_Data, CustomUser, User_Default_Blue_Salvage_Rates, User_Default_Green_Salvage_Rates, User_Default_Yellow_Salvage_Rates, Raw_User_Bank_Data, Raw_User_Inventory_Data,Raw_User_Shared_Inventory_Data, User_Bank, User_Inventory,User_Materials,User_Shared_Inventory, User_Blue_Salvage_Data, User_Green_Salvage_Data, User_Yellow_Salvage_Data
from django.contrib.auth.models import User, Group

class GW2_Recipes_Serializer(serializers.ModelSerializer):
    class Meta:
        model = GW2_Recipes
        fields = ['recipe_id', 'output_id_id', 'output_item_count', 'ingredients']

class GW2_Trading_Post_Data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = GW2_Trading_Post_Data
        fields = ['item_id', 'buys', 'sells']

class GW2_Items_Serializer(serializers.ModelSerializer):
    item_recipe = GW2_Recipes_Serializer(read_only = True)
    item_tp_data = GW2_Trading_Post_Data_Serializer(read_only = True)
    class Meta:
        model = GW2_Items
        fields = ['item_id', 'item_name', 'type', 'rarity', 'vender_value', 'item_recipe', 'item_tp_data']

class CustomUser_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class User_Default_Blue_Salvage_Rates_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Default_Blue_Salvage_Rates
        fields = '__all__'

class User_Default_Green_Salvage_Rates_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Default_Green_Salvage_Rates
        fields = '__all__'

class User_Default_Yellow_Salvage_Rates_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Default_Yellow_Salvage_Rates
        fields = '__all__'
class Raw_User_Shared_Inventory_Data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Raw_User_Shared_Inventory_Data
        fields = '__all__'

class Raw_User_Inventory_Data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Raw_User_Inventory_Data
        fields = '__all__'

class Raw_User_Bank_Data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Raw_User_Bank_Data
        fields = '__all__'

class User_Shared_Inventory_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Shared_Inventory
        fields = '__all__'

class User_Inventory_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Inventory
        fields = '__all__'

class User_Bank_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Bank
        fields = '__all__'

class User_Materials_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Materials
        fields = '__all__'

class User_Blue_Salvage_Data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Blue_Salvage_Data
        fields = '__all__'

class User_Green_Salvage_Data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Green_Salvage_Data
        fields = '__all__'
class User_Yellow_Salvage_Data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Yellow_Salvage_Data
        fields = '__all__'
