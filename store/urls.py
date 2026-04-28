from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . api_views import (
    ProductViewSet,
    OrderViewSet,
    OrderItemViewSet,
    CustomerViewSet,
    ShippingAddressViewSet
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'shipping', ShippingAddressViewSet)

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    #API path
    path('api/', include(router.urls)),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]