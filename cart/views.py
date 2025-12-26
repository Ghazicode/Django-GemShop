from django.shortcuts import render, redirect
from django.views import View
from product.models import Product
from .cart_module import Cart
from .models import Account, Order, OrderItem
from account.models import User




class CartDetailView(View): 
    def get(self, request):
        cart = Cart(request)
        
        return render(request, "cart/cart.html", {'cart':cart})



    def post(self, request):
        account = Account
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gameid = request.POST.get('gameid')
        gamename = request.POST.get('gamename')
        body = request.POST.get('body')

        account.objects.create(
            user = request.user,
            name = name,
            phone = phone,
            email = email, 
            password = password, 
            gameid = gameid, 
            gamename = gamename,
            body = body
            )
        
        next_page = request.GET.get('next')
        if next_page:
            return redirect(next_page)

        return redirect("cart:cart_detail")
        # return render(request, 'cart/cart.html', {})



class CartAddView(View):
    def post(self, request, id):
        product = Product.objects.get(id = id)
        quantity = request.POST.get('quantity')
        cart = Cart(request)
        cart.add(product, quantity)
        return redirect('cart:cart_detail')
    


class CartDeleteView(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)
        return redirect('cart:cart_detail')
    





class OrderDetailView(View):
    
    def get(self, request, pk):
        account = Account.objects.filter(user = request.user).last()
        orders = Order.objects.filter(id = pk,  user = request.user)
        
        orders.update(account = account)
        
        order = Order.objects.get(id = pk)
        
        

        
        

        return render(request, "cart/order_detail.html", {'order':order})
    
    
    



class OrderCreationView(View):
    def get(self, request):
        cart = Cart(request)
        account = Account.objects.filter(user = request.user).last()
        order = Order.objects.create(user = request.user, total_price = int(cart.total()), account = account)
        for item in cart:
            OrderItem.objects.create(order = order, product = item['product'], quantity = item['quantity'], price = item['price'])

        

        cart.remove_cart()

        return redirect('cart:order_detail', order.id)



def pay(request):
    return render(request, 'cart/pay.html')