# Generated by Django 3.2 on 2023-01-28 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_media_media_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='post_id',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
