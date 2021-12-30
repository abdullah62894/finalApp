from django.urls import path, include
from .views import *

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'store'
urlpatterns = [
    # Two List views for RM Code and Name
    path('RMCodelist/', RMCodeslist.as_view(), name='RMCodeList'),
    path('Materiallist/', MaterialNameslist.as_view(), name='MaterialList'),
    # Two Get views for Raw material by RM Code and Name
    path('GetbyRMNo/<str:RMCode>/', GetRMbyCodeNo.as_view(), name='GetRawmaterialbyRMNo'),
    path('GetbyMaterial/<str:Material>/', GetRMbyName.as_view(), name='GetbyMaterialName'),
    # Post view for Raw materials
    path('InsertRawMaterial/', InsertRawMaterials.as_view(), name='InsertRawMaterial'),

    # Demand Table Views for GET & POST
    path('GetDemandbyDNo/<str:DNo>/', GetDemands.as_view(), name='GetDemand'),
    path('GetLatestDemand/', GetLatestDemanded.as_view(), name='GetLatestDemand'),
    path('InsertDemand/', InsertDemand.as_view(), name='InsertDemand'),

    # Demanded Items Table  Views for GET & POST
    path('GetDemandedMaterialsbyDNo/<str:DNo>/', GetDemandedMaterials.as_view(), name='GetDemandedMaterialsbyDNo'),
]



