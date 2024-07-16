from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('view-users', views.CustomUser_List_ViewSet.as_view(), name="view_users"),
    path('view-raw-data', views.GET_User_Raw_Data_View, name="view_raw-data"),
    path('create-record', views.POST_User_Salvage_Outcome_Data_View, name="create-record"),
    path('create-manual-record', views.Manual_User_Salvage_Outcome_Data_View, name="create-manual-record"),
    path('salvage-record/list', views.User_Salvage_Record_ViewSet.as_view({'get':'list'})),
    path('salvage-record/update/<int:pk>', views.User_Salvage_Record_ViewSet.as_view({'patch':'partial_update'})), 
    path('salvage-record/delete/<int:pk>', views.User_Salvage_Record_ViewSet.as_view({'delete':'destroy'})), #TODO: test implementation
    path('outcome-data/list', views.User_Outcome_Data_ViewSet.as_view({'get':'list'})),
    path('outcome-data/update/<int:pk>', views.User_Outcome_Data_ViewSet.as_view({'patch':'partial_update'})),
]