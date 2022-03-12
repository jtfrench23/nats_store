from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('owner/add_product', views.add_product, name="add_product"),
    path('edit/product/<int:id>', views.edit_product, name="edit_product"),
    path('delete/product/<int:id>', views.delete_product, name="delete_product"),
    path('product_manager', views.product_manager),
    path('owner', views.owner_login),
    path('register_owner', views.register_owner),
    path('validate_owner', views.validate_owner_login),
    path('logout', views.logout),
    path('show/product/<int:id>', views.show_product)
]
