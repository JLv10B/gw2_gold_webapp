from django.test import TestCase, Client
from unid_processing.models import CustomUser, User_Salvage_Rates, User_Outcome_Data, User_Salvage_Records
from datetime import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# class User_Salvage_Records_Test(TestCase):
    
#     def setUp(self):
#         self.user = CustomUser.objects.create(username = 'test_test', password = 'password', api_key = '123qweasd')
#         self.salvage_record = User_Salvage_Records.objects.create(user = self.user, salvaged_date = datetime.now(), salvaged_item_id = 1, salvaged_item_count = 1)

#     def test_salvage_record_patch(self):
#         """
#         Test for salvage record partial update using API. 
    
#         """
#         #TODO: response status returning 404 vs 200
#         record = self.salvage_record
#         url = f'/salvage-record/update/{record.pk}'
#         response = self.client.patch(url, salvaged_item_id = 10)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(record.salvaged_item_id, 10)




