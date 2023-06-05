from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LoginView.logout, name="logout"),
    path('signup/', CustomerSignupView.as_view(), name="customerSignup"),
    path('vendorSignup/', VendorSignupView.as_view(), name="vendorSignup"),
    path('customerProfile/', CustomerProfileView.as_view(), name="customerProfile"),
    path('vendorProfile/', VendorProfileView.as_view(), name="vendorProfile"),
    path('vendor/<int:id>/', VendorPageView.as_view(), name="vendorPage"),
    path('aboutUs/', AboutUsView.as_view(), name="aboutUs"),
    path('orders/', ordersPageView.as_view(), name="orders"),
    path('checkout/<int:id>/', checkoutView.as_view(), name="checkout")
]
