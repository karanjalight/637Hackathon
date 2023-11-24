import json

import stripe

from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.conf import settings
from django.views import View
from django.http import JsonResponse

from django.shortcuts import  render, redirect


from .models import Course



class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CourseListView, self).get_context_data(*args, **kwargs)
        return context

    def render_to_response(self, context, **response_kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(CourseListView, self).render_to_response(context, **response_kwargs)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CourseDetailView, self).get_context_data(*args, **kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

    def render_to_response(self, context, **response_kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(CourseDetailView, self).render_to_response(context, **response_kwargs)



stripe.api_key =  'sk_test_51NecLpCn3yES92jn7hNnZlKpT1BLOLKSmtnDm7TJCx5JIUjfgKO8iiqjON44oxSeCfQztziHMYPXApKAl0FbKGId00WuPEFAaw'
class CreateStripeCheckoutSessionView(View):
    """
    Create a checkout session and redirect the user to Stripe's checkout page
    """

    def post(self, request, *args, **kwargs):
        price  = Course.objects.get(id=self.kwargs["pk"])
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(price.price) * 100,
                        "product_data": {
                            "name": price.title,
                            "description": price.description,
                            
                        },
                    },
                    "quantity": 1,
                }
            ],
            metadata={"product_id": price.id},
            mode="payment",
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )
        return redirect(checkout_session.url)


class CourseChargeView(View):
     def post(self, request, *args, **kwargs):
        price  = Course.objects.get(id=self.kwargs["pk"])
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(price.price) * 100,
                        "product_data": {
                            "name": price.product.name,
                            "description": price.product.desc,
                            
                        },
                    },
                    "quantity": price.product.quantity,
                }
            ],
            metadata={"product_id": price.id},
            mode="payment",
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )
        return redirect(checkout_session.url)

# helpers

def get_or_create_customer(email, name, token):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    connected_customers = stripe.Customer.list()
    for customer in connected_customers:
        if customer.email == email:
            print(f'{email} found')
            print(token)
            return customer
    print(f'{email} created')    
    return stripe.Customer.create(
        email=email,
        name=name,
        source=token,
    )



def clientAcquisitionView(request):
    
    

    return render(request, 'clientAcquisition.html')  


def projectPlanningView(request):
    
    return render(request, 'projectplanning.html')


def clientCommunicationView(request):
    
    return render(request, 'clientcommunication.html')


def qualityAssuaranceView(request):
    
    return render(request, 'qualityassuarance.html')


def billingView(request):
    
    return render(request, 'billing.html')


def projectClosureView(request):
    
    return render(request, 'projectclosure.html')


def confidentialityView(request):
    
    return render(request, 'confidentiality.html')
