from django.urls import path

from .views import CourseListView, CourseDetailView, CourseChargeView, CreateStripeCheckoutSessionView

from . import views


urlpatterns = [
  path('', CourseListView.as_view(), name='course_list'),
  path('charge/', CourseChargeView.as_view(), name='charge'),
  path('<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
  path(
        "create-checkout-session/<int:pk>/",
        CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
  
]
