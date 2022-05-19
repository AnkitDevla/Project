from django.shortcuts import render
from .models import *


def home(request):
    data = Product.objects.all()
    data = data[::-1]
    return render(request, "index.html", {"Data": data})


def shop(request, mc, sc, br):
    if(mc == 'all' and sc == 'all' and br == 'all'):
        data = Product.objects.all()
    elif(mc != 'all' and sc == 'all' and br == 'all'):
        data = Product.objects.filter(
            maincat=MainCategory.objects.get(name=mc))
    elif(mc == 'all' and sc != 'all' and br == 'all'):
        data = Product.objects.filter(subcat=SubCategory.objects.get(name=sc))
    elif(mc == 'all' and sc == 'all' and br != 'all'):
        data = Product.objects.filter(brand=Brand.objects.get(name=br))
    elif(mc != 'all' and sc != 'all' and br == 'all'):
        data = Product.objects.filter(maincat=MainCategory.objects.get(name=mc),
                                      subcat=SubCategory.objects.get(name=sc))
    elif(mc != 'all' and sc == 'all' and br != 'all'):
        data = Product.objects.filter(maincat=MainCategory.objects.get(name=mc),
                                      brand=Brand.objects.get(name=br))

    elif(mc == 'all' and sc != 'all' and br != 'all'):
        data = Product.objects.filter(brand=Brand.objects.get(name=br),
                                      subcat=SubCategory.objects.get(name=sc))
    else:
        data = Product.objects.filter(maincat=MainCategory.objects.get(name=mc),
                                      brand=Brand.objects.get(name=br),
                                      subcat=SubCategory.objects.get(name=sc))

    maincat = MainCategory.objects.all()
    subcat = SubCategory.objects.all()
    brand = Brand.objects.all()
    return render(request, "shop.html", {"Data": data,
                                         "Maincat": maincat,
                                         "Subcat": subcat,
                                         "Brand": brand,
                                         "MC": mc,
                                         "SC": sc,
                                         "BR": br
                                         })


def product(request,id):
    product = Product.objects.get(id=id)
    return render(request, "product.html",{"Product":product})
