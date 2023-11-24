from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from django.forms import ModelForm

from .models import CustomUser


from apps.courses.models import *

class CustomAdminUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomAdminUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = CustomUser
		fields = ( "name", "email", "is_seller", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class CourseForm(ModelForm):
      class Meta:
            model = Course
            fields = ['title', 'description', 'price', 'fee']