from django.shortcuts import render, get_object_or_404
from product.models import Category, Product





def home(request):
    category = Category.objects.all()
    popular = Product.objects.filter(popular = True)
    return render(request, 'home/index.html', {'categorys':category, 'popular':popular})







