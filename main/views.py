from django.http import HttpResponse, JsonResponse
import requests, json
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from .utils import *
from rest_framework import generics
from django.views import generic
import requests, json


params = {
        'api_version' : 'v15.0',
        'client_id': '**********',
        'client_secret': '**********',
        'grant_type': 'authorization_code',
        'redirect_uri': 'https://127.0.0.1:8000/code/',
        'scope' : "user_profile,user_media,instagram_graph_user_profile,instagram_graph_user_media"
}


def send_auth(request):
    auth_url = f"https://api.instagram.com/oauth/authorize?client_id={params['client_id']}&redirect_uri={params['redirect_uri']}&scope={params['scope']},&response_type=code"
    return render(request, 'main/main.html', context={'auth_url':auth_url})


def success(request):
    return render(request,'main/success.html')

def get_code(request):
    code = request.GET.get('code')
    files2 = {
        'client_id': '*******',
        'client_secret': '******',
        'grant_type': 'authorization_code',
        'redirect_uri': 'https://127.0.0.1:8000/code/',
        'code': code,
    }
    resp = requests.post('https://api.instagram.com/oauth/access_token/', data=files2).json()
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
