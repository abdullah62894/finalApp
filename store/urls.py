from django.urls import path, include
from .views import *

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'store'
urlpatterns = [
    path('RMCode/', RMCodeView.as_view(), name='RMCode'),
    path('MaterialName/', MaterialNameView.as_view(), name='MaterialName'),
    path('RawMaterialInput/', RawMaterialInputAPI.as_view(), name='RawMaterialInput'),
    path('RMDemandView/', RMDemandView.as_view(), name='RMDemandView'),
    path('RMDemandInput/', RMDemandInputAPI.as_view(), name='RMDemandInput'),
    path('DemandedMaterial/', DemandedMaterialDNoView.as_view(), name='DemandedMaterial'),
    path('DemandedMaterialInput/', DemandedMaterialInputAPI.as_view(), name='DemandedMaterialInput'),
]



