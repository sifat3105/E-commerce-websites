# Generated by Django 5.0.6 on 2024-06-11 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_image7'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_logo',
            field=models.CharField(blank=True, null=True),
        ),
    ]
