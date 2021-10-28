from django.urls import path, include

from . import views

urlpatterns = [

    path('',views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

]

#
# application - python back en d- front html/css
# tempalt - html
# static - css, images.
# django-admin

# django framwork -  django  , pyton  Flask ,
#
# language python +  sql lite
#
# programming langauge
#
# path
#
# website
# html/css/js/images/icon / bootstra/jqyer
#
# python vs php vs java   vs javascript
# django vs laraval vs spring vs  MERN stack

