from rest_framework.routers import DefaultRouter
from .views import ProductViewset,ShoppingUserViewset,AddressViewset

router=DefaultRouter()
router.register(prefix='productapi',viewset=ProductViewset,basename='productcrud')
router.register(prefix='userapi',viewset=ShoppingUserViewset,basename='usercrud')
router.register(prefix='addressapi',viewset=AddressViewset,basename='addresscrud')
