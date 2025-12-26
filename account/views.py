from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import LoginForm, RegisterForm
from django.views import View
from .models import User, UserManager as create_user, ContactUs
from cart.models import Order, OrderItem
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy










class UserLogin(View):
    def get(self, request):
        
        if request.user.is_authenticated:
            return redirect('home:main')
        
        
        form = LoginForm()
        
        return render(request, "account/Login.html", {'form':form})
    

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home:main')
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['phone'], password = cd['password'])
            
            if user is not None:
                login(request, user)
                return redirect('home:main')
            else:
                form.add_error('phone', 'شماره تلفن یا رمز خود را اشتباه وارد کرده اید ')
        


        return render(request, "account/Login.html", {'form':form})
    



class UserRegister(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home:main')
        form = RegisterForm()
        return render(request, "account/Register.html", {'form':form})
    

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home:main')
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if User.objects.filter(phone = cd['phone']).exists():
                form.add_error('phone', 'کاربری با این شماره وجود دارد ')
                
            else:
                if cd['password1'] == cd['password2']:
                    user = User.objects.create_user(phone=cd['phone'], password=cd['password1'], fullname=cd['fullname'])
                    login(request, user)
                    return redirect('home:main')
                else:
                    form.add_error('password1', 'رمز ها با یکدیگرد مطابقت ندارند')

                
        
        return render(request, "account/Register.html", {'form':form})





def contact_us(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        ContactUs.objects.create(
            fullname = fullname,
            email = email,
            subject = subject,
            body = body
            )
        return redirect('home:main')
    return render(request, 'account/contact-us.html')

    



def user_panel(request):
    
    order = Order.objects.filter(user = request.user).prefetch_related('items__product')
    return render(request, 'account/user-profile.html', {'order':order})
    





class CustomPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    # تمپلیتی که برای نمایش فرم استفاده می‌شود
    template_name = 'account/user_edit.html'
    
    # پیامی که پس از موفقیت نمایش داده می‌شود
    success_message = "رمز عبور شما با موفقیت تغییر کرد!"
    success_url = reverse_lazy('home:main')


def logout_view(request):
    logout(request)
    return redirect('home:main')
