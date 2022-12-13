from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def index(request):
    products = Product.objects.all().values('product_name','image','product_desc')
    # listing_product = []
    # for product in products:
    #     product_name = product['product_name']
    #     product_desc = product['product_desc']
    #     test_dict = {product_name:product_desc}
    #     listing_product.append(test_dict)
    params = {"products": products}
    return render(request , "shop/index.html", params)

def about(request):
    return render(request , "shop/about.html")
   
def contact(request):
    return HttpResponse("We are at shop contact page")

def tracker(request):
    return HttpResponse("We are at shop tracker page")

def search(request):
    return HttpResponse("We are at shop search page")

def productView(request):
    return HttpResponse("We are at shop product view page")

def checkout(request):
    return HttpResponse("We are at shop checkout page")

def Add(request):
    Pname = request.POST.get("prod-name","default")
    Pdesc = request.POST.get("prod-desc", "default")
    Pcat = request.POST.get("prod-cat" , "category")
    Psubcat = request.POST.get("prod-subcat" ,"sub category")
    Pprice = request.POST.get("prod-price" , 500.00)
    Pimage = request.POST.get("prod-image")
    product = Product.objects.create( product_name = Pname , product_desc = Pdesc , category = Pcat , sub_category = Psubcat , product_price = Pprice , image = Pimage  )
    product.save()
    return render(request, "shop/Add.html" )
