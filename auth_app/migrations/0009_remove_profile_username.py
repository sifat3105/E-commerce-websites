# Generated by Django 5.0.1 on 2024-06-06 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0008_delete_profile_data_profile_display_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]
