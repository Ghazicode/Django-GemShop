from django.shortcuts import render, get_object_or_404
from .models import Product, Category







# برای نمایش محصول
def product(request, id):
    product = Product.objects.get(id=id)
    popular = Product.objects.filter(popular = True)
    return render(request, 'product/product-detail.html', {'product':product, 'popular':popular})





#برای نمایش محصولات زیر مجموعه و فیلتر شدن ان محصول ها بر اساس موجود بودن یا نبودن انها
def category_detail(request, id):
    category = Category.objects.get(id=id)
    product = category.product.filter(status=True)
    return render(request, "product/products.html", {'products':product})





def pricelists(request):
    pricelist = Product.objects.all()
    return render(request, 'product/price-orders.html', {'pricelist':pricelist})





def productnone(request):
    return render(request, 'product/none.html')


