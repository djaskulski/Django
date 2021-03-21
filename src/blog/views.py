from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from .models import Article
from .forms import ArticleModelForm

# Create your views here.


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self):
    #     return '/'


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()  # <blog>/<modelname>_list.html


# def article_detail_view(request, id):
#     obj = get_object_or_404(Article, id=id)
#     context = {
#         "object": obj
#     }
#     return render(request, "articles/article_detail.html", context)


# def article_list_view(request):
#     queryset = Article.objects.all()  # list of objects
#     context = {
#         'object_list': queryset,
#     }
#     return render(request, "articles/article_list.html", context)

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
