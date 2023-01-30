from django.urls import path
from .views import *

urlpatterns = [
    path('post/<int:post_pk>/', ShowPost.as_view(),name='post'),
    path('add_user/', UsersView.as_view(), name='add_user'),
    path('add_media/', MediaView.as_view(), name='add_media'),

]