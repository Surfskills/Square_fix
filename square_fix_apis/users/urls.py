from django.urls import path
from .views import *

urlpatterns = [
    # Other URL patterns
    # path('api/signup/', signup, name='signup'),
    path("users/signup/", signup),
    path("users/user_login/", user_login),
]
