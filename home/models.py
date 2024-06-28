from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class BillingAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=25, null=True, blank=True)


    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state}, {self.postal_code}, {self.country}"

class ShippingAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state}, {self.postal_code}, {self.country}"
    
    

class HeroSlider(models.Model):
    title_small = models.CharField(max_length=255, help_text="Small title above main title")
    title_large = models.CharField(max_length=255, help_text="Main large title")
    title_brand = models.CharField(max_length=255, help_text="Brand title")
    description = models.TextField(help_text="Description under the titles")
    button_text = models.CharField(max_length=100, help_text="Text displayed on the button")
    button_link = models.URLField(max_length=200, help_text="URL that the button links to")
    image = models.ImageField(upload_to='hero_slider/', help_text="Image for the slider")
    
    def __str__(self):
        return self.title_large

