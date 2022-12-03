from django.shortcuts import *
from django.views.generic import *
from django.contrib.auth.mixins import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

from .models import *


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


class Login(LoginView):
    template_name = "registration/login.html"
    success_url = reverse_lazy("list-tweet")


class Logout(LogoutView):
    template_name = "registration/logout.html"


class CreateTweet(LoginRequiredMixin, CreateView):
    model = Tweet
    template_name = 'twitter/create_tweet.html'
    fields = "__all__"
    success_url = reverse_lazy("list-tweet")


class ListTweet(LoginRequiredMixin, ListView):
    model = Tweet
    template_name = 'twitter/list_tweet.html'


class DeleteTweet(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'twitter/delete_tweet.html'
    success_url = reverse_lazy('list-tweet')



class UpdateTweet(LoginRequiredMixin, UpdateView):
    model = Tweet
    fields = "__all__"
    template_name = 'twitter/update_tweet.html'
    success_url = reverse_lazy('list-tweet')


class CreateFeedback(LoginRequiredMixin, CreateView):
    model = Feedback
    fields = "__all__"
    template_name = "twitter/create_feedback.html"
    success_url = reverse_lazy("list-tweet")