from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import GW2_Items, GW2_Recipes, GW2_Trading_Post_Data, CustomUser, User_Default_Blue_Salvage_Rates, User_Default_Green_Salvage_Rates, User_Default_Yellow_Salvage_Rates, Raw_User_Bank_Data, Raw_User_Inventory_Data,Raw_User_Shared_Inventory_Data, User_Bank, User_Inventory,User_Materials,User_Shared_Inventory, User_Default_Salvage_Rates, Raw_User_Storage, Processed_User_Storage

# Register your models here.
admin.site.register(GW2_Items)
admin.site.register(GW2_Recipes)
admin.site.register(GW2_Trading_Post_Data)
admin.site.register(CustomUser)
admin.site.register(User_Default_Salvage_Rates)
admin.site.register(User_Default_Blue_Salvage_Rates)
admin.site.register(User_Default_Green_Salvage_Rates)
admin.site.register(User_Default_Yellow_Salvage_Rates)
admin.site.register(Raw_User_Storage)
admin.site.register(Raw_User_Bank_Data)
admin.site.register(Raw_User_Inventory_Data)
admin.site.register(Raw_User_Shared_Inventory_Data)
admin.site.register(Processed_User_Storage)
admin.site.register(User_Bank)
admin.site.register(User_Inventory)
admin.site.register(User_Materials)
admin.site.register(User_Shared_Inventory)

