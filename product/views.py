from django.shortcuts import render, redirect
from .models import Product, Category, SubCategory
from .utils import convert_to_16_9




def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        old_price = request.POST.get('old_price')
        discount = request.POST.get('discount')
        sku = request.POST.get('sku')
        warranty = request.POST.get('warranty')
        brand = request.POST.get('brand')
        quantity = request.POST.get('quantity')
        category_id = request.POST.get('category')
        subcategory_id = request.POST.get('subcategory')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
        image5 = request.FILES.get('image5')
        image6 = request.FILES.get('image6')
        image7 = request.FILES.get('image7')
        img = request.FILES.get('image')
        image = convert_to_16_9(img)
                
        category = Category.objects.get(id=category_id)
        subcategory = SubCategory.objects.get(id=subcategory_id)
        
        Product.objects.create(
            name=name,
            description=description,
            price=price,
            old_price=old_price,
            sku=sku,
            quantity=quantity,
            category=category,
            subcategory=subcategory,
            image=image,
            image2=image2,
            image3=image3,
            image4=image4,
            image5=image5,
            image6=image6,
            image7=image7,
            warranty=warranty,
            brand=brand,
            discount=discount,
        )
        
        return redirect('create_product')
    
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    return render(request, 'product/create_product.html', {'categories': categories, 'subcategories': subcategories})


def product_view(request):
    products = Product.objects.all()
   
    return render(request, 'product/product_view.html', {'products': products})



def right_product_view(request , uuid):
    product = Product.objects.get(uuid = uuid)

    return render(request, 'product/right_product_view.html', {'product':product})