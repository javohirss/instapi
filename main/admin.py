from django.contrib import admin
from .models import *
# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_id','username' ,'account_type', 'media_count')
    search_fields = ('username',)


class MediaAdmin(admin.ModelAdmin):
    list_display = ('media_id', 'caption', 'media_url', 'media_type', 'timestamp', 'username')
    search_fields = ('username', 'timestamp')


admin.site.register(Users, UsersAdmin)
admin.site.register(Media, MediaAdmin)