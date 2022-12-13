

from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index , name="SHOPHOME"),
    path("about", views.about , name="SHOP ABOUT"),
    path("contact", views.contact , name="SHOP contact"),
    path("tracker", views.tracker , name="SHOP tracker"),
    path("search", views.search , name="SHOP SEARCH"),
    path("productview", views.productView , name="SHOP PRODUCT VIEW"),
    path("checkout", views.checkout , name="SHOP CHECKOUT"),
    path("add", views.Add, name='add')
]