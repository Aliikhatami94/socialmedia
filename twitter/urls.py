from django.urls import path

from .views import *


urlpatterns = [
    path("register/", SignUp.as_view(), name='signup'),
    path("login/", Login.as_view(), name='login'),
    path("logout/", Logout.as_view(), name='logout'),
    path("create/", CreateTweet.as_view(), name='create-tweet'),
    path("", ListTweet.as_view(), name='list-tweet'),
    path("delete/<pk>", DeleteTweet.as_view(), name='delete-tweet'),
    path("update/<pk>", UpdateTweet.as_view(), name='update-tweet'),
    path("comment/", CreateFeedback.as_view(), name='comment'),
]