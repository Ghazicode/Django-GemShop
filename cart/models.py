from django.db import models
from account.models import User
from product.models import Product
from django_jalali.db import models as jmodels
from hashids import Hashids




class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts', null=True, blank=True, verbose_name='کاربر')
    name = models.CharField(max_length=100, verbose_name='نام')
    phone = models.CharField(max_length=11,verbose_name='شماره تلفن')
    email = models.EmailField(verbose_name='ایمیل اکانت')
    password = models.CharField(max_length=200, verbose_name='رمز اکانت')
    gameid = models.CharField(max_length=200, verbose_name='ایدی اکانت')
    gamename = models.CharField(null=True, blank=True, verbose_name='اسم اکانت')
    body = models.TextField(null=True, blank=True, verbose_name='توضیحات')






    class Meta:
        verbose_name = 'اکانت'
        verbose_name_plural = 'اکانت ها'




    def __str__(self):
        return self.email



hashids = Hashids(salt="your-secret-key", min_length=8)

class Order(models.Model):
    STATUS_CHOICES = [
        ('successful', ('موفق')),
        ('waiting', ('در حال بررسی')),
        ('Unsuccessful', ('ناموفق')),
    ]

    

    tracking_code = models.CharField(max_length=50, unique=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.tracking_code:
            # ۳. از آن برای ساخت کد استفاده کنید
            self.tracking_code = hashids.encode(self.id)
            super().save(update_fields=['tracking_code'])


    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='کاربر')
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='waiting', verbose_name='وضعیت')
    total_price = models.IntegerField(default=0, verbose_name='جمع قیمت') 
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='account', null=True, blank=True, verbose_name='اکانت کاربر')
    created_at = jmodels.jDateField(auto_now_add=True, verbose_name='زمان ثبت')
    is_paid = models.BooleanField(default=False, verbose_name='پرداخت')
    



    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'
    



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='سفارشات')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products', verbose_name='محصول')
    quantity = models.SmallIntegerField(default=0, verbose_name='تعداد')
    price = models.PositiveIntegerField(verbose_name='قیمت محصول')






    class Meta:
        verbose_name = 'محصول سبد خرید'
        verbose_name_plural = 'محصولات سبد خرید'

