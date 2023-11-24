from django.urls import path

from .views import StripeAuthorizeView, StripeAuthorizeCallbackView

from . import views



urlpatterns = [
  path('authorize/', StripeAuthorizeView.as_view(), name='authorize'),
  path("register-seller/", views.register_seller, name="register-seller"),
  path("register-buyer/", views.register_buyer, name="register-buyer"),
  path("about_us/", views.about_us, name="about"),

  path('createcourse/', views.createCourse, name="create-course"),
  
  path('oauth/callback/', StripeAuthorizeCallbackView.as_view(), name='authorize_callback'),
]
