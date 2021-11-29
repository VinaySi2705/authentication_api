# from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import UserSerializer,ChangePasswordSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import permissions
from django.contrib.auth.hashers import make_password

#signup of users
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

#change password
class ChangePasswordView(APIView):
    def post(self,request):
        user = User.objects.get(username=request.user.username)
        password = make_password(request.data.get('password'))
        user.password=password
        user.save()
        return Response({"password":"password changed successfully"})


"""
class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self,request):
        serializer =UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

"""
