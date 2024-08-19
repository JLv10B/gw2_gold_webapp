from django.test import TestCase, Client, RequestFactory
from datetime import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, APIRequestFactory, force_authenticate
from unid_processing.models import CustomUser, User_Salvage_Rates, User_Outcome_Data, User_Salvage_Records
from unid_processing.views import User_Salvage_Record_ViewSet, User_Outcome_Data_ViewSet
import json

class CustomUser_Test(APITestCase):
    def setUp(self):
        self.user_info = self.generate_user_info()

    def generate_user_info(self):
        return {
            "username": "fake.user_name",
            "password": "fake.password",
            "email": "example@email.com",
            "api_key": "fake.api_key",
        }
    
    def test_create_user(self):
        """
        Test for creating users using API. 
    
        """
        c = Client()
        url = '/auth/users/'
        response = c.post(url, self.user_info)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = CustomUser.objects.get(id = 1)
        self.assertEqual(user.email, self.user_info["email"])
        self.assertEqual(user.username, self.user_info["username"])
        self.assertEqual(user.api_key, self.user_info["api_key"])
        self.assertNotEqual(user.password, self.user_info["password"]) # Passwords should not be equal due to hashing


class User_Salvage_Records_Test(APITestCase):
    
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = CustomUser.objects.create(username = 'test_test', password = 'password', api_key = '123qweasd', is_active = True)
        self.salvage_record = User_Salvage_Records.objects.create(user = self.user, salvaged_date = '2024-07-29T17:47:05.180814Z', salvaged_item_id = 1, salvaged_item_count = 1)

    def test_salvage_record_check(self):
        """
        Testing User_Salvage_Records model. 
    
        """
        record = self.salvage_record
        self.assertTrue(isinstance(record, User_Salvage_Records))
        self.assertEqual(record.user, CustomUser.objects.get(username = 'test_test'))
        self.assertEqual(record.salvaged_item_id, 1)
        self.assertEqual(record.salvaged_item_count, 1)

    def test_salvage_record_get(self):
        """
        Test for salvage record get call. 
    
        """
        view = User_Salvage_Record_ViewSet.as_view({'get':'list'}) 
        url = reverse('salvage-record-list')
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, 200)

class User_Outcome_Data_Test(APITestCase):

    def setUp(self):
            self.factory = APIRequestFactory()
            self.client = APIClient()
            self.user = CustomUser.objects.create(username = 'test_test', password = 'password', api_key = '123qweasd', is_active = True)
            self.salvage_record = User_Salvage_Records.objects.create(user = self.user, salvaged_date = '2024-07-29T17:47:05.180814Z', salvaged_item_id = 1, salvaged_item_count = 1)
            self.outcome_data = User_Outcome_Data.objects.create(record_number = self.salvage_record, gained_item_id = 2, gained_item_count = 2)

    def test_outcome_data_check(self):
        """
        Testing User_Outcome_Data model. 
    
        """
        record = self.outcome_data
        self.assertTrue(isinstance(record, User_Outcome_Data))
        self.assertEqual(record.record_number, self.salvage_record)
        self.assertEqual(record.gained_item_id, 2)
        self.assertEqual(record.gained_item_count, 2)

    def test_salvage_record_get(self):
        """
        Test for outcome data get call. 
    
        """
        #TODO: How do I add request.data['record_number']?
        view = User_Outcome_Data_ViewSet.as_view({'get':'list'}) 
        url = reverse('outcome-data-list')
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, 200)