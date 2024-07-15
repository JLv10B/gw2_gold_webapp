from rest_framework import serializers
from .models import CustomUser, User_Salvage_Rates, User_Salvage_Records, User_Outcome_Data
from django.contrib.auth.models import User, Group

class CustomUser_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class User_Salvage_Recod_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Salvage_Records
        fields = '__all__'

class User_Salvage_Recod_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Outcome_Data
        fields = '__all__'
