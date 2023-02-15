from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import CategorySerializer,ProductSerializer,SubcategorySerializer,ShoppingUserSerializer,AddressSerializer,ShoppingCartSerializer,CartItemSerializer,OrderSerializer
from rest_framework.decorators import api_view
from .models import Category,Subcategory,Product,ShoppingUser,Address,ShoppingCart,CartItem,Order
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser,FileUploadParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@api_view(['GET'])
@csrf_exempt
def Hello(request):
    # return JsonResponse("Hello",safe=False)
    data=['Hi']
    return Response(data)

@api_view(['GET'])
def Categories(request):
    categories=Category.objects.all()
    serializer=CategorySerializer(categories,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Products(request):
    products=Product.objects.all()
    
    serializer=ProductSerializer(products,many=True)
    print(serializer)
    return Response(serializer.data)


@api_view(['GET'])
def ProductDetail(request,id):
    product=Product.objects.get(id=id)
    serializer=ProductSerializer(product,many=False)
    return Response(serializer.data)

# @api_view(['POST'])
# @parser_classes([FileUploadParser,MultiPartParser])
# def ProductCreate(request):
#     serializer=ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)



@api_view(['GET'])
def ProductSubcategory(request,id):
    product=Product.objects.get(id=id)
    # myJson={
    #     "name":"Haaland",
    #     "job":"footballer"
    # }
    
    # print("Hi")
    return Response(product.subcategory.name)
    # return Response(myJson)
@api_view(['GET'])
def ProductsInSubcategory(request,subcategory):
    # product=Product.objects.filter(subcategory=subcategory)
    # serializer=ProductSerializer(product,many=True)
    c=[]
    for item in Product.objects.all():
        if item.subcategory.name.lower()==subcategory.lower():
            c.append(item)
    serializer=ProductSerializer(c,many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def ProductsInCategory(request,category):
    # product=Product.objects.filter(subcategory=subcategory)
    # serializer=ProductSerializer(product,many=True)
    c=[]
    for item in Product.objects.all():
        if item.subcategory.category.name.lower()==category.lower():
            c.append(item)
    serializer=ProductSerializer(c,many=True)
    
    return Response(serializer.data)

class ProductViewset(ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    
@api_view(['GET'])

def ProductSearch(request,keyword):
    c=[]
    for item in Product.objects.all():
        if  item.name.lower().startswith(keyword.lower()) or keyword.lower() == item.subcategory.name.lower() or keyword.lower() == item.subcategory.category.name.lower():
            c.append(item)
        
    serializer=ProductSerializer(c,many=True)
    return Response(serializer.data)
              
class ShoppingUserViewset(ModelViewSet):
    queryset=ShoppingUser.objects.all()
    serializer_class=ShoppingUserSerializer
    def retrieve(self, request, *args, **kwargs):
        instance=self.get_object()
        print(type(instance.address))
        print(instance.address.id)
        address_instance=Address.objects.get(id=instance.address.id)    
        address_serializer=AddressSerializer(address_instance)
        print(address_serializer.data)
        # id=instance.address
        # instance.address=Address.objects.get(id)
        serializer=ShoppingUserSerializer(instance,many=False)
        # print(serializer1.data['address'])
        serializer_data=serializer.data
        
        serializer_data['address']=address_serializer.data
        print(serializer_data['address'])
        
        return Response(serializer_data)
    
    
class AddressViewset(ModelViewSet):
    queryset=Address.objects.all()
    serializer_class=AddressSerializer
    

@api_view(['GET'])
def Get_Cart(request,userId):
    try:
        query_set=ShoppingCart.objects.get(pk=userId)
    except:
        return Response({'msg':'this user does not have a cart'},status=status.HTTP_404_NOT_FOUND)
        
    
    serializer=ShoppingCartSerializer(query_set,many=False)
    dict1=serializer.data
    print(dict1)
    
    cart_items=CartItem.objects.all().filter(cart=userId)
    serializer1=CartItemSerializer(cart_items,many=True)
    dict2=serializer1.data
    dict_list=[]
    for item in dict2:
        dict_list.append(dict(item))
        
    print(dict_list)
    
    dict1['items']=dict_list
    return Response(dict1)
    # return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])   
def CreateCart(request,userId):
    try:
        query_set=ShoppingCart.objects.get(pk=userId)
        return Response({'msg':'User already has a cart'})
    except:
        user=ShoppingUser(pk=userId)
        cart=ShoppingCart(user=user)
        cart.save()
        
        return Response({'msg':'cart created for '+user.username})
    
    pass
@api_view(['GET'])
def Get_CartItem(request,userId,cartItemId):
        try:
            query_set=CartItem.objects.get(pk=cartItemId,cart=userId)
        except:
            return Response({'msg':'this user does not have a cart'},status=status.HTTP_404_NOT_FOUND)
        # cart_item=query_set.objects.get(pk=cartItemId)
        # serializer=CartItemSerializer(cart_item,many=False)
        # return Response(serializer.data)
        print(type(query_set))
        serializer=CartItemSerializer(query_set,many=False)
        return Response(serializer.data)

@api_view(['GET'])
def Add_CartItem(request,userId,productId):
    if CartItem.objects.all().filter(product=productId,cart=userId):
        # a=CartItem.objects.get(product=productId,cart=userId).quantity
        # CartItem.objects.update(product=productId,cart=userId,quantity=a+1)
        cartitem=CartItem.objects.get(product=productId,cart=userId)
        cartitem.quantity+=1
        cartitem.save()
    
    else:
        product=Product.objects.get(pk=productId)
        cart=ShoppingCart.objects.get(user=userId)
        my_cart_item=CartItem(product=product,cart=cart,quantity=1)
        my_cart_item.save()
        
    query_set=CartItem.objects.get(product=productId,cart=userId)
    serializer=CartItemSerializer(query_set)
    return Response(serializer.data)    
    # return Response({'msg':'Hi'})
@api_view(['DELETE'])
def DeleteCartItem(request,userId,productId):
    try:
        cartitem=CartItem.objects.get(product=productId,cart=userId)
        cartitem.delete()
        return Response({'msg':'Cart item deleted'})
    except:
        return Response({'msg':'Cart item does not exist in cart'})
@api_view(['GET'])
def GetOrderHistory(request,userId):
    try:
        orders=Order.objects.filter(cart=userId)
        if orders:
            serializer=OrderSerializer(orders,many=True)
            return Response(serializer.data)
        else:
            return Response({"msg":'user does not have order'})
    except:
        return Response({'msg':'we have an error'})

@api_view(['GET','POST'])
def CreateOrder(request,userId):
    cart=ShoppingCart.objects.get(user=userId)
    order=Order(cart=cart,order_status='shipping')
    order.save()
    return Response(order)

   
       
        
        
    
     

    


# @api_view(['GET'])
# def Categories(request):
    