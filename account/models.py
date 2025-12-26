from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, phone, fullname, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone:
            raise ValueError("Users must have an phone address")

        user = self.model(
            phone = phone,
            fullname=fullname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, fullname, password=None):
        
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone,
            password=password,
            fullname = fullname,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    REQUIRED_FIELDS = ['fullname']
    phone = models.CharField(max_length=11, unique=True, verbose_name='phone')
    fullname = models.CharField(max_length=70, verbose_name='fullname')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)



    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'




    objects = UserManager()

    USERNAME_FIELD = "phone"

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    




class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='کاربر')
    fullname = models.CharField(max_length=100, null=True, blank=True, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(null=True, blank=True, verbose_name='ایمیل')
    subject = models.CharField(max_length=100, null=True, blank=True, verbose_name='موضوع')
    body = models.TextField(null=True, blank=True, verbose_name='پیام')


    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'