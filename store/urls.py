from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('shirts', views.shirts),
    path('earrings', views.earrings),
    path('signs', views.signs),
    path('owner/add_product', views.add_product, name="add_product"),
    path('edit/product/<int:id>', views.edit_product, name="edit_product"),
    path('delete/product/<int:id>', views.delete_product, name="delete_product"),
    path('product_manager', views.product_manager),
    path('owner', views.owner_login),
    path('register_owner', views.register_owner),
    path('validate_owner', views.validate_owner_login),
    path('logout', views.logout),
    path('show/product/<int:id>', views.show_product),
    path('login', views.login_register),
    path('register/submit', views.register_customer),
    path('login/user', views.login_user),
    path('orders', views.orders),
    path('delete/order/<int:id>', views.order_delete),
    path('ship/<int:id>', views.ship),
    path('undo_ship/<int:id>', views.undo_ship),
    path('message', views.message_form),
    path('send/message', views.send_message),
    path('view_messages', views.view_messages),
    path('view/message/<int:id>', views.view_one_message),
    path('delete/message/<int:id>', views.delete_message),
]
