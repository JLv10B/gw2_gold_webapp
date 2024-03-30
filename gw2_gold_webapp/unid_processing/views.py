from django.shortcuts import render
import requests
# Create your views here.

# hyperbrand
# key = 'E0812565-299A-F848-8651-595EDAAB30CA6B3DAE04-6CF3-4DF5-8E2F-B7823D5EA333'
# malstram.1236
key = 'C99F7BA6-5B0F-FB42-912A-85101D23163F1C9922E7-E3B7-4043-B603-969DF9F025C8' 

all_account_characters = requests.get(f'https://api.guildwars2.com/v2/characters/?access_token={key}')
character_inventory_items = requests.get(f'https://api.guildwars2.com/v2/characters/Trashbandit Mal/inventory?access_token={key}')
account_bank_items = requests.get(f'https://api.guildwars2.com/v2/account/inventory?access_token={key}')
# print(all_account_characters.text)
print(character_inventory_items.text)
# print(account_bank_items.text)
# for char in account_bank_items:
    # print(char)
