from django.db import models
from django.utils.text import slugify




class Category(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='عنوان')
    image = models.ImageField(upload_to='categorys', verbose_name='عکس')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
       return self.title
    



class Product(models.Model):
    gamename = models.CharField(max_length=200, verbose_name='اسم بازی')
    category = models.ManyToManyField(Category, related_name='product', verbose_name='دسته بندی')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    discount = models.SmallIntegerField(null=True, blank=True, verbose_name='تخفیف')
    image = models.ImageField(upload_to='products', verbose_name='عکس')
    status = models.BooleanField(default=True,verbose_name='وضعیت')
    popular = models.BooleanField(default=False, verbose_name='محبوب')
    

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'




    def __str__(self):
        return self.title