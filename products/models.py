from django.db import models
from PIL import Image
from django.contrib.auth.models import UserManager,AbstractUser

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(to=Subcategory, on_delete=models.SET_NULL,null=True)
    
    price=models.IntegerField(null=True)
    image=models.ImageField(("image"), upload_to="prod/images", height_field=None, width_field=None, max_length=None,default="")
    
    
    
    def __str__(self) -> str:
        return self.name
    
    
class ShoppingUserManager(UserManager):
    pass 

class Address(models.Model):
    
    street=models.TextField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=6)
    
    def __str__(self) -> str:
        return "Address "+str(self.id)

    
    

class ShoppingUser(AbstractUser):
    phone_no=models.CharField(max_length=10)
    objects=ShoppingUserManager()
    address=models.OneToOneField(Address,on_delete=models.SET_NULL,null=True,blank=True)
    
    class Meta(AbstractUser.Meta):
        swappable="AUTH_USER_MODEL"
    def __str__(self) -> str:
        return self.username  
    

    
    
class ShoppingCart(models.Model):
    user=models.OneToOneField(ShoppingUser,on_delete=models.CASCADE,primary_key=True)
    created_time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username +"'s cart"
    
class CartItem(models.Model):
    product=models.OneToOneField(Product,on_delete=models.CASCADE,primary_key=True)
    quantity=models.IntegerField(default=0)
    cart=models.ForeignKey(ShoppingCart,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.name+" cart item"
    
class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    cart=models.OneToOneField(ShoppingCart,on_delete=models.PROTECT)
    order_status=models.CharField(max_length=50)
    order_fulfilled=models.BooleanField(default=False)
    
    def __str__(self):
        return self.cart.user.username+"'s order"
    

     


