from django.shortcuts import render
from .models import GW2_Recipes
from .serializer import GW2_Recipes_Serializer
import requests
# Create your views here.

# hyperbrand
key = 'E0812565-299A-F848-8651-595EDAAB30CA6B3DAE04-6CF3-4DF5-8E2F-B7823D5EA333'
# malstram.1236
# key = 'C99F7BA6-5B0F-FB42-912A-85101D23163F1C9922E7-E3B7-4043-B603-969DF9F025C8' 
recipe_id = 1
all_account_characters = requests.get(f'https://api.guildwars2.com/v2/characters/?access_token={key}')
character_inventory_items = requests.get(f'https://api.guildwars2.com/v2/characters/Trashbandit Mal/inventory?access_token={key}')
account_bank_items = requests.get(f'https://api.guildwars2.com/v2/account/inventory?access_token={key}')
all_recipes = requests.get(f'https://api.guildwars2.com/v2/recipes')
single_recipe = requests.get(f'https://api.guildwars2.com/v2/recipes/{recipe_id}')
# print(all_account_characters.text)
# print(character_inventory_items.text)
# print(account_bank_items.text)
# print(all_recipes.text)
print(single_recipe.json())
print(type(single_recipe.json()))
# for char in account_bank_items:
    # print(char)

def GW2_recipes_PUT_GET(request, recipe_id = None):
    """
    This function accepts put and get requests. 
    
    Put = updates all recipes
    Get = returns recipes in recipe_id_list
    """
    if request.method == "GET":
        all_recipe_json = requests.get(f'https://api.guildwars2.com/v2/recipes')
        recipe_id_list = all_recipe_json.json()
        for recipe_id in recipe_id_list:
            recipe_request = requests.get(f'https://api.guildwars2.com/v2/recipes/{recipe_id}')
            recipe = recipe_request.json()
            serialized_recipe = GW2_Recipes_Serializer(data = recipe)
            serialized_recipe.is_valid()
            serialized_recipe.save()

    if request.method == "GET":
        
        
    
    
    
    

# Testing:
# if __name__ == "__main__":
    # fetch_GW2_recipes()