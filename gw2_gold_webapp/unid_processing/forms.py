from django.forms import ModelForm
from .models import CustomUser

class UsterCreationForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'api_key']

