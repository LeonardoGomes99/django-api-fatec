from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.models import User
from products.models import Product
from orders.models import Order

from django.contrib.auth.hashers import make_password

from .serializers import UsersSerializer, ProductsSerializer, OrdersSerializer

from rest_framework.permissions import IsAuthenticated
from oauth2_provider.decorators import protected_resource

# USUARIO
@protected_resource(scopes=['read'])
@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UsersSerializer(user)
    return Response(serializer.data)

@protected_resource(scopes=['read'])
@api_view(['GET'])
def getUserAll(request):
    items = User.objects.all()
    serializer = UsersSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        user_data = serializer.validated_data
        user_data['password'] = make_password(user_data['password'])
        user = serializer.save(**user_data)
    return Response(serializer.data, status=201)

@protected_resource(scopes=['read'])
@api_view(['PUT'])
def updateUser(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UsersSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@protected_resource(scopes=['read'])
@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return Response({'message': 'Usuario Removido com Sucesso !!!'})



# PRODUTO
@protected_resource(scopes=['read'])
@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductsSerializer(product)
    return Response(serializer.data)

@protected_resource(scopes=['read'])
@api_view(['GET'])
def getProductAll(request):
    items = Product.objects.all()
    serializer = ProductsSerializer(items, many=True)
    return Response(serializer.data)

@protected_resource(scopes=['read'])
@api_view(['POST'])
def addProduct(request):
    serializer = ProductsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=201)

@protected_resource(scopes=['read'])
@api_view(['PUT'])
def updateProduct(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductsSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@protected_resource(scopes=['read'])
@api_view(['DELETE'])
def deleteProduct(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return Response({'message': 'User deleted successfully'})



# PEDIDO
@protected_resource(scopes=['read'])
@api_view(['GET'])
def getOrder(request, pk):
    order = Order.objects.get(pk=pk)
    serializer = OrdersSerializer(order)
    return Response(serializer.data)

@protected_resource(scopes=['read'])
@api_view(['GET'])
def getOrderAll(request):
    items = Order.objects.all()
    serializer = OrdersSerializer(items, many=True)
    return Response(serializer.data)

@protected_resource(scopes=['read'])
@api_view(['POST'])
def addOrder(request):
    serializer = OrdersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=201)

@protected_resource(scopes=['read'])
@api_view(['PUT'])
def updateOrder(request, pk):
    order = Order.objects.get(pk=pk)
    serializer = OrdersSerializer(order, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@protected_resource(scopes=['read'])
@api_view(['DELETE'])
def deleteOrder(request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return Response({'message': 'User deleted successfully'})

