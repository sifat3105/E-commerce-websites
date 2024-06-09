# from django.shortcuts import render
# from .models import Category, SubCategory

# # Create Categories
# categories = [
#     "Electronics", "Fashion", "Home and Kitchen", "Beauty and Personal Care", 
#     "Sports and Outdoors", "Books and Media", "Toys and Games", 
#     "Health and Wellness", "Automotive", "Office Supplies", 
#     "Pet Supplies", "Baby and Kids"
# ]

# for category_name in categories:
#     Category.objects.create(name=category_name)

# # Create SubCategories
# electronics = Category.objects.get(name='Electronics')
# fashion = Category.objects.get(name='Fashion')

# subcategories = [
#     {'name': 'Smartphones', 'category': electronics},
#     {'name': 'Laptops', 'category': electronics},
#     {'name': 'Men\'s Clothing', 'category': fashion},
#     {'name': 'Women\'s Clothing', 'category': fashion},
# ]

# for subcategory in subcategories:
#     SubCategory.objects.create(name=subcategory['name'], category=subcategory['category'])


