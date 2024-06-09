from django.shortcuts import render, redirect
from .models import Product, Category, SubCategory
from .utils import convert_to_16_9


def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        sku = request.POST.get('sku')
        quantity = request.POST.get('quantity')
        category_id = request.POST.get('category')
        subcategory_id = request.POST.get('subcategory')
        img = request.FILES.get('image')
        image = convert_to_16_9(img)
                
        category = Category.objects.get(id=category_id)
        subcategory = SubCategory.objects.get(id=subcategory_id)
        
        Product.objects.create(
            name=name,
            description=description,
            price=price,
            sku=sku,
            quantity=quantity,
            category=category,
            subcategory=subcategory,
            image=image,
        )
        
        return redirect('create_product')
    
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    return render(request, 'product/create_product.html', {'categories': categories, 'subcategories': subcategories})


def product_view(request):
    products = Product.objects.all()
   
    return render(request, 'product/product_view.html', {'products': products})



# myapp/views.py
# myapp/views.py
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
# from .utils import convert_to_16_9
import os

def upload_and_convert_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        
        # Paths for input and output images
        input_image_path = os.path.join(fs.location, filename)
        output_image_path = os.path.join(fs.location, f"converted_{filename}")
        
        # Convert image to 16:9
        convert_to_16_9(input_image_path, output_image_path)
        
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'converted_file_url': fs.url(f"converted_{filename}")
        })
    return render(request, 'upload.html')

