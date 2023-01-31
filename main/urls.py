from django.urls import path
from .views import *

urlpatterns = [
    path('', send_auth, name='mainpage'),
    path('success/', success, name='success_page'),
    path('post/<int:post_pk>/', ShowPost.as_view(),name='post'),
    path('add_user/', UsersView.as_view(), name='add_user'),
    path('add_media/', MediaView.as_view(), name='add_media'),
    path('code/', get_code, name='code'),

]