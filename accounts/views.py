import datetime
import jwt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from rest_framework_simplejwt import models
from django.db import models
from .models import User
from .serializers import RegisterSerializer,loginSerializer, UserSerializer, PasswordSerializer,ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate,login,logout
from rest_framework import generics, mixins, permissions,  status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class loginUser(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = loginSerializer

    def post(self, request):
        serializer = loginSerializer(data=request.data)
        if serializer.is_valid():
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    payload = {
                        'id': user.id,
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                        'iat': datetime.datetime.now()
                    }
                    token = jwt.encode(payload, 'secret',algorithm='HS256')
                    #login(request, user)
                    response = Response()

                    response.set_cookie(key='jwt',value=token,httponly=True)
                    response.data = {'jwt': token,
                                     'role': user.role
                                     }

                    return response
                else:
                    return Response("account not found")
            else:
                return Response("failed login")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):

    def get(self,request):
        token = request.COOKIES.get('jwt')

        if not token:
            return Response("User not logged in")
        try:
            payload = jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response("User not logged in")

        user = User.objects.get(pk=payload['id'])
        serializer = UserSerializer(user, many=False)

        return Response(serializer.data)

class logoutView(APIView):

    def post(self,request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message' : 'succes'
        }

        return response


class ChangePassword(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer

    def put(self, request, *args, **kwargs):
        token = request.COOKIES.get('jwt')

        if not token:
            return Response("User not logged in")
        try:
            payload = jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response("User not logged in")

        user = User.objects.get(pk=payload['id'])
        self.object = user
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]},
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = Response()
            response.delete_cookie('jwt')
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

