from rest_framework import serializers
from products.models import Category, Subcategory, Product,ShoppingUser,Address,ShoppingCart,CartItem,Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


# class SubcategorySerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
#     category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

#     class Meta:
#         model = Subcategory
#         fields = ('id', 'name', 'category','category_id')
        
#     def create(self, **validated_data):
#         category_data=validated_data.pop('category')
#         category=Category.objects.create(**category_data)
#         subcategory=Subcategory.objects.create(category=category,**validated_data)
        
class SubcategorySerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'category')
        
    

# class ProductSerializer(serializers.ModelSerializer):
#     subcategory = SubcategorySerializer()
#     subcategory_id = serializers.PrimaryKeyRelatedField(queryset=Subcategory.objects.all())

#     class Meta:
#         model = Product
#         # fields = ('id', 'name', 'subcategory','image')
#         fields=('id','name','subcategory','price','subcategory_id','image')
        
#     def create(self, validated_data):
#         subcategory_data = validated_data.pop('subcategory')
#         subcategory = SubcategorySerializer.create(self,**subcategory_data)
#         product=Product.objects.create(subcategory=subcategory,**validated_data)
#         return product
class ProductSerializer(serializers.ModelSerializer):
    # subcategory = SubcategorySerializer()
    # subcategory_id = serializers.PrimaryKeyRelatedField(queryset=Subcategory.objects.all())

    class Meta:
        model = Product
        # fields = ('id', 'name', 'subcategory','image')
        fields=('id','name','subcategory','price','image')
        
    # def create(self, validated_data):
    #     subcategory_data = validated_data.pop('subcategory')
    #     subcategory = SubcategorySerializer.create(self,**subcategory_data)
    #     product=Product.objects.create(subcategory=subcategory,**validated_data)
    #     return product
    
class AddressSerializer (serializers.ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'
class ShoppingUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=ShoppingUser
        # fields=['username','first_name','last_name','phone_no']
        fields='__all__'

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model=ShoppingCart
        fields='__all__'
        
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields="__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"
    
    

    