# Generated by Django 5.0.1 on 2024-06-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0003_remove_profile_display_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='forget_otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
            ],
        ),
    ]
