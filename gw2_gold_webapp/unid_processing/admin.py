from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import GW2_Crafting_Recipes, GW2_Items, GW2_Trading_Post_Data, CustomUser, User_Salvage_Rates, User_Shared_Inventory_Data, User_Inventory_Data, User_Bank_Data, User_Materials_Data,User_Wallet_Data, User_Salvage_Results

# Register your models here.
admin.site.register(GW2_Items)
admin.site.register(GW2_Crafting_Recipes)
admin.site.register(GW2_Trading_Post_Data)
admin.site.register(CustomUser)
admin.site.register(User_Salvage_Rates)
admin.site.register(User_Shared_Inventory_Data)
admin.site.register(User_Inventory_Data)
admin.site.register(User_Bank_Data)
admin.site.register(User_Materials_Data)
admin.site.register(User_Wallet_Data)
admin.site.register(User_Salvage_Results)


