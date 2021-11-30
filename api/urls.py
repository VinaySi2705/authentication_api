from django.urls import path,include
from .views import RegisterView, ChangePasswordView

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    path('password_reset/', include('django_rest_passwordreset.urls'), name='password_reset'),
]
