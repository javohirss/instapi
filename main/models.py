from django.db import models
from django.urls import reverse

# Create your models here.

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=50, null=True, unique=True)
    access_token = models.CharField(max_length=255, null=True, unique=True)
    account_type = models.CharField(max_length=255, null=True)
    media_count = models.IntegerField(null=True)
    username = models.CharField(max_length=255, unique=True, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('post', kwargs= {'pk' : self.pk})

class Media(models.Model):
    media_id = models.AutoField(primary_key=True)
    caption = models.TextField()
    id = models.CharField(max_length=50, null=True, unique=True)
    media_url = models.URLField(max_length=1000,default='')
    media_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    username = models.ForeignKey('Users', on_delete=models.CASCADE)

    def __str__(self):
        return self.media_type

