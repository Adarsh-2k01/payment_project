"""payment_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from swiftcash import views

urlpatterns = [
    path('admin/', admin.site.urls),
#open page url.
    path('LS/', views.LoginandSignup),
    
 #firstpage url..
    path('select/',views.select),
#bank page url...
    path('bank/',views.bank),
    path('selfbank/',views.selfbank),
    path('form_fillup/',views.form_fillup),
    path('otp/',views.otp),
    path('done/',views.done),
#credit/debit page url....
    path('card/',views.card),
    path('CDverify/',views.CDverify),
    path('rent/', views.rent),
    path('house_rent/', views.house_rent),
    path('shop_rent/', views.shop_rent),
    path('social_main/', views.social_main),
#electricity page url.....
    path('EB/',views.EB),
#dth page url......
    path('DTH/',views.DTH),
    path('dth_payment',views.dth_payment),
#recharge page url.......
    path('Recharge/',views.Recharge),
    path('recharge_payment/',views.recharge_payment),
    path('contact/',views.contact),
    

]
