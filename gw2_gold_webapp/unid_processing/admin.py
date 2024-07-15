from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, User_Salvage_Rates, User_Salvage_Records, User_Outcome_Data

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(User_Salvage_Records)
admin.site.register(User_Outcome_Data)
admin.site.register(User_Salvage_Rates)

