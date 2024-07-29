from rest_framework import serializers
from .models import CustomUser, User_Salvage_Rates, User_Salvage_Records, User_Outcome_Data
from django.contrib.auth.models import User, Group
from djoser.serializers import UserCreateSerializer


# class CustomUser_Serializer(UserCreateSerializer): # Testing out overriding Djoser's UserCreateSerializer
#     class Meta():
#         model = CustomUser
#         fields = '__all__'

class CustomUser_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class User_Salvage_Record_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Salvage_Records
        fields = '__all__'

class User_Outcome_data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Outcome_Data
        fields = '__all__'

class User_Salvage_Rate_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Salvage_Rates
        fields = '__all__'
