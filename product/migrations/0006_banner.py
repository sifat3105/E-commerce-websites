# Generated by Django 5.0.1 on 2024-06-28 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_category_cat_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_small', models.CharField(help_text='Small title above main title', max_length=255)),
                ('title_large', models.TextField(help_text='Main large title')),
                ('image', models.ImageField(help_text='Image for the banner', upload_to='banners/')),
                ('button_text', models.CharField(help_text='Text displayed on the button', max_length=100)),
                ('button_link', models.URLField(help_text='URL that the button links to')),
            ],
        ),
    ]