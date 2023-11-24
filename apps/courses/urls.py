from django.urls import path

from .views import (CourseListView, CourseDetailView, CourseChargeView, CreateStripeCheckoutSessionView,
                    clientAquisitionView, projectPlanningView, clientCommunicationView, qualityAssuaranceView,
                    billingView, projectClosureView, confidentialityView)

from . import views


urlpatterns = [
  path('', CourseListView.as_view(), name='course_list'),
  path('charge/', CourseChargeView.as_view(), name='charge'),
  path('<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
  path("create-checkout-session/<int:pk>/",CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
  path("client-acquisition/<int:pk>", clientAquisitionView, name="client-acquisition" ),
  path("project-planning/<int:pk>", projectPlanningView, name="project-planning"),
  path("client-communication/<int:pk>", clientCommunicationView, name="client-communication"),
  path("quality-assuarance/<int:pk>", qualityAssuaranceView, name="quality-assuarance"),
  path("billing", billingView, name="billing"),
  path("project-closure/<int:pk>", projectClosureView, name="project-closure"),
  path("confidentiality", confidentialityView, name="confidentiality"),
    
]
