from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .router import router

urlpatterns = [
    path("",views.Hello),
    path("category/",views.Categories),
    path("products/",views.Products),
    path("products/getById/<str:id>/",views.ProductDetail),
    path("products/getById/<str:id>/subcategory",views.ProductSubcategory),
    path("products/subcategory/<str:subcategory>",views.ProductsInSubcategory),
    path("products/category/<str:category>",views.ProductsInCategory),
    path("productapi/subcategory/<str:subcategory>",views.ProductsInSubcategory),
    path("productapi/category/<str:category>",views.ProductsInCategory),
    path("productapi/search/<str:keyword>",views.ProductSearch),
    path("cart/<str:userId>/getCart",views.Get_Cart),
    path("cart/<str:userId>/createCart",views.CreateCart),
    path("cart/<str:userId>/getCartItem/<str:cartItemId>",views.Get_CartItem),
    path("cart/<str:userId>/add/<str:productId>",views.Add_CartItem),
    path("cart/<str:userId>/remove/<str:productId>",views.DeleteCartItem),
    path("order/<str:userId>/getOrders",views.GetOrderHistory),
    path("order/<str:userId>/createOrder",views.CreateOrder)
    # path("products/createproduct/",views.ProductCreate)
    
    
    
    
   
]+router.urls
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

