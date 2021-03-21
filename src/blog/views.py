from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.


def article_detail_view(request, id):
    obj = get_object_or_404(Article, id=id)
    context = {
        "object": obj
    }
    return render(request, "articles/article_detail.html", context)


def article_list_view(request):
    queryset = Article.objects.all()  # list of objects
    context = {
        'object_list': queryset,
    }
    return render(request, "articles/article_list.html", context)

# def product_create_view(request):
#     initial_data = {
#         'title': "Gold title of your choice",
#         'description': "Produced in: Composition:",
#         'email': "your_mail@edu.com"
#     }
#     form = ProductForm(request.POST or None, initial=initial_data)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#
#     context = {
#         'form': form,
#     }
#     return render(request, "products/product_create.html", context)
#
#
# def product_delete_view(request, id):
#     obj = get_object_or_404(Product, id=id)
#     # POST request
#     if request.method == "POST":
#         obj.delete()
#         return redirect('../../')
#     context = {
#         "object": obj
#     }
#     return render(request, "products/product_delete.html", context)
