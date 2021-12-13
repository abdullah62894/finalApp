from django.urls import path, include
from .views import *

from accounts.views import RegisterView,loginUser, UserView, logoutView,ChangePassword
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'Account'
urlpatterns = [

    path('login/', loginUser.as_view(), name='login'),
    path('logout/', logoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('changepassword/', ChangePassword.as_view(), name='changepassword'),
    path('userv/', UserView.as_view(), name='userv'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

]