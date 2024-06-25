from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('data_dump/', views.data_dump_view, name="data_dump"),
    path('view-users', views.CustomUser_List_ViewSet.as_view(), name="view_users"),
    path('create-user', views.CustomUser_Create_ViewSet.as_view(), name="create_user"),

]