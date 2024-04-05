from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.    
class GW2_Recipes(models.Model):
    recipe_id = models.IntegerField(unique = True)
    output_item_id = models.IntegerField(primary_key = True)
    output_item_count = models.IntegerField()
    ingredients = models.JSONField()

    def __str__(self) -> str:
        return (f'{self.output_item_id} recipe')

class GW2_Trading_Post_Data(models.Model):
    item_id = models.IntegerField(primary_key = True, unique = True)
    buys = models.JSONField()
    sells = models.JSONField()

    def __str__(self) -> str:
        return (f'{self.item_id} trading post data')

class GW2_Items(models.Model):
    item_id = models.IntegerField(primary_key = True, unique = True)
    item_name = models.CharField(max_length = 200)
    type = models.CharField(max_length = 200)
    rarity = models.CharField(max_length = 200)
    venter_value = models.IntegerField(null = True, blank = True)
    item_recipe = models.OneToOneField(GW2_Recipes, related_name = 'item', on_delete = models.SET_NULL, blank = True, null = True)
    item_tp_data = models.OneToOneField(GW2_Trading_Post_Data, related_name = 'item', on_delete = models.SET_NULL, blank = True, null = True)

    def __str__(self) -> str:
        return self.item_name

class CustomUser(AbstractUser):
    username = models.CharField(max_length = 40, unique = True)
    password = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    api_key = models.CharField(max_length = 100)

    def __str__(self):
        return self.username
    
class User_Default_Salvage_Rates(models.Model):
    # TODO: Convert rarity to choice field
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    item_id = models.IntegerField(primary_key = True, unique = True)
    item_name = models.ForeignKey(GW2_Items, on_delete = models.CASCADE)
    rarity = models.CharField()
    salvage_rate = models.DecimalField(max_digits = 4, decimal_places = 2, null = True)

    def __str__(self) -> str:
        return (f'item = {self.item_name}, salvage rate = {self.salvage_rate}')


class _Raw_User_Storage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True)
    id = models.IntegerField(primary_key = True)
    name = models.ForeignKey(GW2_Items, on_delete = models.CASCADE)
    count = models.IntegerField(null = True)

class Raw_User_Shared_Inventory_Data(_Raw_User_Storage):
    pass

class Raw_User_Inventory_Data(_Raw_User_Storage):
    pass

class Raw_User_Bank_Data(_Raw_User_Storage):
    pass

class _Processed_User_Storage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True)
    id = models.IntegerField(primary_key = True, unique = True)
    name = models.ForeignKey(GW2_Items, on_delete = models.CASCADE)
    count = models.IntegerField(null = True)

class User_Shared_Inventory(_Processed_User_Storage):
    # Note: aggragate stacks of the same items when deserializing
    pass

class User_Inventory(_Processed_User_Storage):
    # Note: aggragate stacks of the same items when deserializing
    pass

class User_Bank(_Processed_User_Storage):
    # Note: aggragate stacks of the same items when deserializing
    pass

class User_Materials(_Processed_User_Storage):
    pass

class User_Salvage_Results(models.Model):
    # TODO: Convert rarity to choice field
    username = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    salvaged_item_count = models.IntegerField()
    item_id = models.IntegerField()
    rarity = models.CharField()
    item_count = models.IntegerField()




