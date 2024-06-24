from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.    
class GW2_Crafting_Recipes(models.Model):
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
    venter_value = models.IntegerField(null = True, blank = True)

    def __str__(self) -> str:
        return self.item_name

class User(AbstractUser):
    username = models.CharField(max_length = 40, unique = True)
    password = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    api_key = models.CharField(max_length = 100)

    def __str__(self):
        return self.username
    
class _User_Storage(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    time_recorded = models.DateTimeField(auto_now_add = True)
    item_id = models.IntegerField()
    item_count = models.IntegerField(null = True)

class User_Shared_Inventory_Data(_User_Storage):
    pass

class User_Inventory_Data(_User_Storage):
    pass

class User_Bank_Data(_User_Storage):
    pass

class User_Materials_Data(_User_Storage):
    pass

class User_Wallet_Data(_User_Storage):
    currency_id = models.IntegerField(primary_key = True)

class User_Salvage_Records(models.Model):
    record_number = models.IntegerField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    salvaged_date = models.DateTimeField()
    salvaged_item_id = models.IntegerField()

    def __str__(self) -> str:
        return (f'record number = {self.record_number}, salvaged item = {self.salvaged_item_id}')

class User_Outcome_Data(models.Model):
    record_number = models.ForeignKey(User_Salvage_Records, on_delete = models.CASCADE)
    gained_item_id = models.ForeignKey(GW2_Items, on_delete= models.CASCADE)
    gained_item_count = models.IntegerField()

    def __str__(self) -> str:
        return (f'item = {self.gained_item_id}, count = {self.gained_item_count}')
    
class User_Salvage_Rates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gained_item_id = models.ForeignKey(GW2_Items, on_delete=models.CASCADE)
    blue_salvage_rate = models.DecimalField()
    green_salvage_rate = models.DecimalField()
    yellow_salvage_rate = models.DecimalField()

    def __str__(self) -> str:
        return (f'blue slavage rate = {self.blue_salvage_rate}\n 
                green salvage rate = {self.green_salvage_rate}\n 
                yellow salvage rate = {self.yellow_salvage_rate}')


