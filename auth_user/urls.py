from django.urls import path
from auth_user.views import Singin, Singup, ProfileEdit

urlpatterns = [
    path('singup/', Singup.as_view(), name='singup'),
    path('singin/', Singin.as_view(), name='singin'),
    path('edit/', ProfileEdit.as_view(), name='edit'),
]
