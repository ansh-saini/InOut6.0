from django.urls import path, include
from django.conf.urls import include, url
from . import views
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    url(r'^paypal/',include('paypal.standard.ipn.urls')),
    path('payment', views.payment, name='payment'),

]