from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Gw2_Items(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 200)
    type = models.CharField(max_length = 200)
    rarity = models.CharField(max_length = 200)
    venter_value = models.IntegerField(null = True, blank = True)

    def __str__(self) -> str:
        return self.name

class CustomUser(AbstractUser):
    username = models.CharField(max_length = 40, unique = True)
    password = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    api_key = models.CharField(max_length = 100)

    def __str__(self):
        return self.username
    
class User_Default_Salvage_Rates(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    id = models.IntegerField(primary_key = True)
    name = models.ForeignKey(Gw2_Items, on_delete = models.CASCADE)
    salvage_rate = models.DecimalField(max_digits = 4, decimal_places = 2, null = True)

    def __str__(self) -> str:
        return (f'item = {self.name}, salvage rate = {self.salvage_rate}')

class User_Default_Blue_Salvage_Rates(User_Default_Salvage_Rates):
    pass

class User_Default_Green_Salvage_Rates(User_Default_Salvage_Rates):
    pass

class User_Default_Yellow_Salvage_Rates(User_Default_Salvage_Rates):
    pass

class Raw_User_Storage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    id = models.IntegerField(primary_key = True)
    name = models.ForeignKey(Gw2_Items, on_delete = models.CASCADE)
    count = models.IntegerField(null = True)

class Raw_User_Shared_Inventory_Data(Raw_User_Storage):
    pass

class Raw_User_Inventory_Data(Raw_User_Storage):
    pass

class Raw_User_Bank_Data(Raw_User_Storage):
    pass

class Processed_User_Storage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    id = models.IntegerField(primary_key = True, unique = True)
    name = models.ForeignKey(Gw2_Items, on_delete = models.CASCADE)
    count = models.IntegerField(null = True)

class User_Shared_Inventory(Processed_User_Storage):
    # Note: aggragate stacks of the same items when deserializing
    pass

class User_Inventory(Processed_User_Storage):
    # Note: aggragate stacks of the same items when deserializing
    pass

class User_Bank(Processed_User_Storage):
    # Note: aggragate stacks of the same items when deserializing
    pass

class User_Materials(Processed_User_Storage):
    pass

class Trading_Post_Data(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.ForeignKey(Gw2_Items, on_delete = models.CASCADE)
    buys = models.JSONField(null = True, blank = True)
    sells = models.JSONField(null = True, blank = True)
