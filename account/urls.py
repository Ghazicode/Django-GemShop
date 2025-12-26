from django.urls import path
from . import views


app_name = "account"
urlpatterns=[
    path('user', views.user_panel, name='user'),
    path('login', views.UserLogin.as_view(), name='login'),
    path('register', views.UserRegister.as_view(), name='register'),
    path('contact', views.contact_us, name='contact'),
    path('edit', views.CustomPasswordChangeView.as_view(), name='edit'),
    path('logout', views.logout_view, name='logout'),

    
]