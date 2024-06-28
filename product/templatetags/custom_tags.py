# from django import template
# from ..models import Category

# register = template.Library()

# @register.inclusion_tag('product/category.html')
# def load_categories():
#     categories = Category.objects.all()
#     for cat in categories:
#         print(cat)
#     return {'categories': categories, 'cat':cat}