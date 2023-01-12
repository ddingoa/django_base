from django.urls import path
from ddingouser.views import UserCreateView

urlpatterms = [
    path('v1/users/create/',UserCreateView.as_view(), name='apis_v1_user'),
]

