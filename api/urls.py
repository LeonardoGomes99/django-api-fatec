from django.urls import path
from . import views

urlpatterns = [
  path('users/<int:pk>', views.getUser),
  path('users/all',views.getUserAll),
  path('users/add',views.addUser),
  path('users/update/<int:pk>', views.updateUser),
  path('users/delete/<int:pk>', views.deleteUser),

  path('products/<int:pk>', views.getProduct),
  path('products/all',views.getProductAll),
  path('products/add',views.addProduct),
  path('products/update/<int:pk>', views.updateProduct),
  path('products/delete/<int:pk>', views.deleteProduct),

  path('orders/<int:pk>', views.getOrder),
  path('orders/all',views.getOrderAll),
  path('orders/add',views.addOrder),
  path('orders/update/<int:pk>', views.updateOrder),
  path('orders/delete/<int:pk>', views.deleteOrder),
]