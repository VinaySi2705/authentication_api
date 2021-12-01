# from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import UserSerializer#,ChangePasswordSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import permissions
from django.contrib.auth.hashers import make_password
from rest_framework.authentication import BasicAuthentication

# reset password email
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "go to http://127.0.0.1:8000/password_reset/confirm/ and there post token and new password",
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )


#signup of users
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

#change password
class ChangePasswordView(APIView):
    authentication_classes = [BasicAuthentication]
    def post(self,request):
        user = User.objects.get(username=request.user.username)
        password = make_password(request.data.get('password'))
        user.password=password
        user.save()
        return Response({"password":"password changed successfully",
                          "login":"http://127.0.0.1:8000/accounts/login/"})

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
