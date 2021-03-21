"""Django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import (
    mindfulness_view,
    minimalism_view,
    recycling_view,
    vegetarianism_view,
    yoga_view,
    contact_view,
    about_view
)
from mindfulness.views import (
    product_detail_view,
    product_create_view,
    product_delete_view,
    product_list_view,
)

urlpatterns = [
    path('', about_view, name='about'),

    path('products/', product_list_view, name='product-list'),
    path('products/<int:id>/', product_detail_view, name='product-detail'),
    path('products/<int:id>/delete/', product_delete_view, name='product-delete'),
    path('create/', product_create_view, name='product-create'),

    path('mindfulness/', mindfulness_view, name='mindfulness'),
    path('minimalism/', minimalism_view, name='minimalism'),
    path('recycling/', recycling_view, name='recycling'),
    path('vegetarianism/', vegetarianism_view, name='vegetarianism'),
    path('yoga/', yoga_view, name='yoga'),
    path('contact/', contact_view, name='contact'),
    path('admin/', admin.site.urls),
]
