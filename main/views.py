from django.http import HttpResponse, JsonResponse
import requests, json
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from rest_framework import generics
from django.views import generic
import requests, json
# Create your views here.

params = {
        'api_version' : 'v15.0',
        'client_id': '1122889231709880',
        'client_secret': '48e193436a1a2562f86ba0b36d517e77',
        'grant_type': 'authorization_code',
        'redirect_uri': 'https://127.0.0.1:8000/code/',
        'code': 'YOUR GENERATED CODE',
        'scope' : "user_profile,user_media,instagram_graph_user_profile,instagram_graph_user_media"
}



# Для получения токена и id
# response = requests.post('https://api.instagram.com/oauth/access_token/', data=files2)
# print(response.json())
account1_token = "YOUR TOKEN"
accoint1_id = 'YOUR ID'
account2_token = "YOUR TOKEN"
accoint2_id = 'YOUR ID'


getting_user_data = requests.get("https://graph.instagram.com/v15.0/17841408001271089?fields=id,account_type,media_count,username&access_token=YOUR_TOKEN")
getting_media_data = requests.get('https://graph.instagram.com/YOUR_ID/media?fields=id,caption,media_url,media_type,username,timestamp&access_token=YOUR_TOKEN')
# Here I am taking the data manually and passing it to the form also manually due to an issue with getting tokens automatically


def exchange_token_to_long(token):
    return requests.get(f"https://graph.instagram.com/access_token?grant_type=ig_exchange_token&client_secret={params['client_secret']}&access_token={token}").json()['access_token']

def get_user_data(id, token):
    return requests.get(f"https://graph.instagram.com/{params['api_version']}/{id}?fields=id,account_type,media_count,username&access_token={token}").json()

def get_media_data(id, token):
    return requests.get(f'https://graph.instagram.com/{id}/media?fields=id,caption,media_url,media_type,username,timestamp&access_token={token}').json()

def send_auth(request):
    auth_url = f"https://api.instagram.com/oauth/authorize?client_id={params['client_id']}&redirect_uri={params['redirect_uri']}&scope={params['scope']},&response_type=code"
    return render(request, 'main/main.html', context={'auth_url':auth_url})


def success(request):
    return render(request,'main/success.html')

def get_code(request):
    code = request.GET.get('code')
    files2 = {
        'client_id': '1122889231709880',
        'client_secret': '48e193436a1a2562f86ba0b36d517e77',
        'grant_type': 'authorization_code',
        'redirect_uri': 'https://127.0.0.1:8000/code/',
        'code': code,
    }
    resp = requests.post('https://api.instagram.com/oauth/access_token/', data=files2).json()
    token, id = resp['access_token'], resp['user_id']
    token = exchange_token_to_long(token)
    user_data = get_user_data(id, token)|{'access_token':token}
    media_data = get_media_data(id, token)
    print(user_data)
    print(media_data)
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

# def show_post(request, post_pk):
#     post = get_object_or_404(Users, pk=post_pk)
#
#     # return HttpResponse(f"{post_pk}")
#     return render(request, 'main/post.html', context={'post' : post})
#
# def mainView(request):
#     print([f.name for f in Users._meta.get_fields()])
#     user_data = requests.get('https://graph.instagram.com/17841444949437417/media?fields=id,caption,media_url,media_type,username,timestamp&access_token=IGQVJYcnAtRC1WMk9xdG9OMEZA4UFV6UlNKWkVDMWd5dVUwQU5FbjVzbjJuZAjhCSU5FVWdPMC12ampENnpIaW1NektYZAGNsYkg5UkYzcTc0WVFHUmdId2xsT3F3dDN3NVdPaTlNNktB')
#     return JsonResponse(resp2.json())

# def user_view(request):
#     if request.POST:
#         form = UserForm(request.POST)
#
#     else:
#         form = UserForm
#
#     return render(request, 'main/users.html', context={'form' : form})

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
