from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here. 
class CustomUser(AbstractUser):
    api_key = models.CharField(max_length=100, blank = True)

    REQUIRED_FIELDS = ['api_key']


class User_Salvage_Records(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    salvaged_date = models.DateTimeField()
    salvaged_item_id = models.IntegerField(default=0)
    salvaged_item_count = models.IntegerField(default=0)

class User_Outcome_Data(models.Model):
    record_number = models.ForeignKey(User_Salvage_Records, on_delete = models.CASCADE)
    gained_item_id = models.CharField(max_length=100, blank = True)
    gained_item_count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return (f'item = {self.gained_item_id}, count = {self.gained_item_count}')
    
    class Meta:
        unique_together = ('record_number', 'gained_item_id')
    
class User_Salvage_Rates(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    gained_item_id = models.CharField(max_length=100, blank = True)
    blue_salvage_rate = models.DecimalField(max_digits=5, decimal_places=2)
    green_salvage_rate = models.DecimalField(max_digits=5, decimal_places=2)
    yellow_salvage_rate = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('user', 'gained_item_id')


