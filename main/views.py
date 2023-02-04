from django.http import HttpResponse, JsonResponse
import requests, json
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from .utils import *
from rest_framework import generics
from django.views import generic
import requests, json

from django.conf import settings

def send_auth(request):
    auth_url = f"https://api.instagram.com/oauth/authorize?client_id={settings.INSTAGRAM_API_SETTINGS['client_id']}&redirect_uri={settings.INSTAGRAM_API_SETTINGS['redirect_uri']}&scope={settings.INSTAGRAM_API_SETTINGS['scope']},&response_type=code"
    return render(request, 'main/main.html', context={'auth_url':auth_url})


def success(request):
    return render(request,'main/success.html')

def get_code(request):
    code = request.GET.get('code')
    data = {
        **settings.INSTAGRAM_API_SETTINGS,
        "code":code
        }
    resp = requests.post('https://api.instagram.com/oauth/access_token/', data=data).json()
    token, id = resp['access_token'], resp['user_id']
    token = exchange_token_to_long(token)
    user_data = get_user_data(id, token)|{'access_token':token}
    media_data = get_media_data(id, token)
    Users.objects.create(**user_data)
    for post in media_data['data']:
        username = Users.objects.get(username=post.pop('username'))
        Media.objects.create(username=username,**post)
    return redirect(reverse('success_page'))

class ShowPost(generic.DetailView):
    model = Users
    template_name = 'main/post.html'
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'


class UsersView(generic.CreateView):
    form_class = UserForm
    template_name = 'main/users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Adding users'
        return context



class MediaView(generic.CreateView):
    form_class = MediaForm
    template_name = 'main/media.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Adding media'
        return context
