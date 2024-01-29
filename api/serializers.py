from rest_framework import serializers
from users.models import User
from products.models import Product
from orders.models import Order

class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = '__all__'