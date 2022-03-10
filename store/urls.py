from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('add_image',views.add_image),
    path('owner/add_product', views.add_product, name="add_product"),
    path('edit/product/<int:id>', views.edit_product, name="edit_product"),
    path('delete/product/<int:id>', views.delete_product, name="delete_product"),
    path('product_manager', views.product_manager)
]
