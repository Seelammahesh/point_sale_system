"""
URL configuration for point_sale_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from datarepo.views import add_category, list_category, update_category, delete_category,add_subcategory,list_subcategory,update_subcategory,delete_subcategory,add_product,list_products,update_product,delete_product
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_category/',add_category,name="add_category"),
    path('list_category/',list_category,name="list_category"),
    path('update_category/',update_category,name="update_category"),
    path('delete_category/',delete_category,name="delete_category"),
    #sub_categories
    path('add_subcategory/',add_subcategory,name="add_subcategory"),
    path('list_subcategory/',list_subcategory,name="list_subcategory"),
    path('update_subcategory/',update_subcategory,name="update_subcategory"),
    path('delete_subcategory/',delete_subcategory,name="delete_subcategory"),
    #products
    path('add_product/',add_product,name="add_product"),
    path('list_products/',list_products,name="list_products"),
    path('update_product/',update_product,name="update_product"),
    path('delete_product/',delete_product,name="delete_product"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

