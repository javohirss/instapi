from django.http import HttpResponse, JsonResponse
import requests, json
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from rest_framework import generics
from django.views import generic
import requests, json
# Create your views here.

files2 = {
        'client_id': 'CLIENT_ID',
        'client_secret': 'CLIENT_SECRET',
        'grant_type': 'authorization_code',
        'redirect_uri': 'REDIRECT_URI',
        'code': 'YOUR GENERATED CODE',
}

# Для получения токена и id
# response = requests.post('https://api.instagram.com/oauth/access_token/', data=files2)
# print(response.json())
#истекает через 60 дней начиная с 26.01.2022
account1_token = "YOUR TOKEN"
accoint1_id = 'YOUR ID'
account2_token = "YOUR TOKEN"
accoint2_id = 'YOUR ID'


getting_user_data = requests.get("https://graph.instagram.com/v15.0/17841408001271089?fields=id,account_type,media_count,username&access_token=YOUR_TOKEN")
getting_media_data = requests.get('https://graph.instagram.com/YOUR_ID/media?fields=id,caption,media_url,media_type,username,timestamp&access_token=YOUR_TOKEN')
# Here I am taking the data manually and passing it to the form also manually due to an issue with getting tokens automatically



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
