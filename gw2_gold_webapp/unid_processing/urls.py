from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('view-users', views.CustomUser_List_ViewSet.as_view(), name="view_users"),
    path('view-raw-data', views.GET_User_Raw_Data_View, name="view_raw-data"),

]