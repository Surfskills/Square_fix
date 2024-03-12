from django.urls import path
from .views import signup

urlpatterns = [
    # Other URL patterns
    # path('api/signup/', signup, name='signup'),
    path("users/signup/", signup),
]
