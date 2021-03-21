from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm


# Create your views here.
def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


def product_list_view(request):
    queryset = Product.objects.all()  # list of objects
    context = {
        'object_list': queryset,
    }
    return render(request, "products/product_list.html", context)


def product_create_view(request):
    initial_data = {
        'title': "Gold title of your choice",
        'description': "Produced in: Composition:",
        'email': "your_mail@edu.com"
    }
    form = ProductForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, "products/product_create.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # POST request
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)

# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     # context = {
#     #     "title": obj.title,
#     #     "description": obj.description,
#     #     "price": obj.price,
#     # }
#     context = {
#         'object': obj,
#     }
#     return render(request, "products/product_detail.html", context)


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#
#     context = {
#         'form': form,
#     }
#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == "POST":
#         title = request.POST.get('title')
#         print(title)
#         # Product.objects.create(title=new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)
