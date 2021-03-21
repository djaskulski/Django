from django.urls import path
from blog.views import (
    article_detail_view,
    article_list_view,
)

urlpatterns = [
    path('', article_list_view, name='article-list'),
    path('<int:id>/', article_detail_view, name='article-detail'),
    # path('<int:id>/delete/', product_delete_view, name='product-delete'),
    # path('create/', product_create_view, name='product-create')
]