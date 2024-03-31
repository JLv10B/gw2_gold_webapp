from rest_framework import serializers
from .models import GW2_Items, GW2_Recipes, GW2_Trading_Post_Data, CustomUser, User_Default_Blue_Salvage_Rates, User_Default_Green_Salvage_Rates, User_Default_Yellow_Salvage_Rates, Raw_User_Bank_Data, Raw_User_Inventory_Data,Raw_User_Shared_Inventory_Data, User_Bank, User_Inventory,User_Materials,User_Shared_Inventory
from django.contrib.auth.models import User, Group

class GW2_Recipes_Serializer(serializers.ModelSerializer):
    class Meta:
        model = GW2_Recipes
        fields = ['id', 'output_id_id', 'output_item_count', 'ingredients']

class GW2_Trading_Post_Data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = GW2_Trading_Post_Data
        fields = ['id', 'buys', 'sells']

class GW2_Items_Serializer(serializers.ModelSerializer):
    # To Do: 
    # Test if this works, this may take excessive amount of time.
    # Read more on if we need to specify fields explicity, when do I need to specify, and how it really works
    item_recipe = GW2_Recipes_Serializer()
    item_tp_data = GW2_Trading_Post_Data_Serializer()
    class Meta:
        model = GW2_Items
        fields = ['id', 'name', 'type', 'rarity', 'vender_value', 'item_recipe', 'item_tp_data']

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
