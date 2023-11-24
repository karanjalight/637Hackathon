import urllib

import requests

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.conf import settings
from django.shortcuts import redirect

from .models import *

from django.shortcuts import  render
from .forms import NewUserForm, CourseForm
from django.contrib.auth import login
from django.contrib import messages


from apps.courses.models import *
""" 
def dashboard(request):

    if request.method == "POST":

        form = courseForm(request.POST)
        print("=============== 1. form posting====================")
	
        seller = request.user
        print(seller)
	
   

    return render(request, "create-course.html", {"form": form})
 """

def CreateCourse(request):
	if request.method == 'POST':
		form = CourseForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = CourseForm()
	return render(request, 'create-course.html', { 'form': form})		
        


#2.49 am code!
#Line [url = 'redirect_uri': f'http://localhost:8000/users/oauth/callback']
class StripeAuthorizeView(View):

    def get(self, request):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        url = 'https://connect.stripe.com/oauth/authorize'
        params = {
            'response_type': 'code',
            'scope': 'read_write',
            'client_id': settings.STRIPE_CONNECT_CLIENT_ID,
            'redirect_uri': f'http://localhost:8000/users/oauth/callback'
        }
        url = f'{url}?{urllib.parse.urlencode(params)}'
        return redirect(url)


class StripeAuthorizeCallbackView(View):

    def get(self, request):
        code = request.GET.get('code')
        if code:
            data = {
                'client_secret': settings.STRIPE_SECRET_KEY,
                'grant_type': 'authorization_code',
                'client_id': settings.STRIPE_CONNECT_CLIENT_ID,
                'code': code
            }
            url = 'https://connect.stripe.com/oauth/token'
            resp = requests.post(url, params=data)
            # add stripe info to the seller
            stripe_user_id = resp.json()['stripe_user_id']
            #####################
            print(stripe_user_id)
           # payouts = "schedule"
            #delay_days: 7
            #interval: int(1)
	    
            #print(payouts)
            #print(delay_days)


            stripe_access_token = resp.json()['access_token']
            print(stripe_access_token)
            seller = Seller.objects.filter(user_id=self.request.user.id).first()
            
            seller.stripe_user_id = stripe_user_id
            seller.stripe_access_token = stripe_access_token
            seller.save()
            
        url = reverse('home')
        response = redirect(url)
        return response
    


def register_seller(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('home')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def register_buyer(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('home')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registerBuyer.html", context={"register_form":form})


def about_us(request):
	
	return render (request=request, template_name="aboutUs.html")

#-----------------------------------------------
#-CREATE NEW COURSE
def createCourse(request):
	if request.method == 'POST':
		post = Course()
		post.title = request.POST['title']
		post.description = request.POST['description']
		post.price = request.POST['price']
		post.seller = Seller.objects.filter(user_id=request.user.id).first()
        
		print("======================================")
		post.save()	
		return redirect('home')
	
	else:
		return render(request, 'createCourse.html')

	
