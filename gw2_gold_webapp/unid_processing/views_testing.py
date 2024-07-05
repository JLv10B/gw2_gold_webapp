from django.shortcuts import render
import requests
from django.http import HttpResponse
import json

# hyperbrand
key = 'E0812565-299A-F848-8651-595EDAAB30CA6B3DAE04-6CF3-4DF5-8E2F-B7823D5EA333'
# malstram.1236
# key = 'C99F7BA6-5B0F-FB42-912A-85101D23163F1C9922E7-E3B7-4043-B603-969DF9F025C8' 

# recipe_id = 1
# all_account_characters = requests.get(f'https://api.guildwars2.com/v2/characters/?access_token={key}')
# character_inventory_items = requests.get(f'https://api.guildwars2.com/v2/characters/Hyper Brand/inventory?access_token={key}')
# account_bank_items = requests.get(f'https://api.guildwars2.com/v2/account/inventory?access_token={key}')
# all_recipes = requests.get(f'https://api.guildwars2.com/v2/recipes')
# single_recipe = requests.get(f'https://api.guildwars2.com/v2/recipes/{recipe_id}')

# char_list = requests.get(f'https://api.guildwars2.com/v2/characters/?access_token={key}').json()

# id_and_count_dict = []
# for char in char_list:
#     char_inventory = requests.get(f'https://api.guildwars2.com/v2/characters/{char}/inventory?access_token={key}').json()
#     bag_list = char_inventory['bags']
#     for specific_bag in bag_list:
#         bag_contents = specific_bag['inventory']
#         for bag_slot in bag_contents:
#             if bag_slot != None:
#                 item_id = bag_slot['id']
#                 item_count = bag_slot['count']

#                 id_and_count_dict.append({item_id:item_count})
# print(id_and_count_dict)

def get_vals(test_dict, key_list):
    result_dict = {}
    stack = [test_dict]
     
    while stack:
        current_dict = stack.pop()
        print(current_dict)
        for k, v in current_dict.items():
            if k in key_list:
                result_dict[k] = v
            elif isinstance(v, dict):
                stack.append(v)
     
    return result_dict
 

    
    
    
# Testing:
if __name__ == "__main__":
    test_dict = {'gfg': {'is': {'best' : 3}}, 'for': {'all' : 4}, 'geeks': 5}
    key_list = ['best', 'geeks']
    res = get_vals(test_dict, key_list)
    print(res)