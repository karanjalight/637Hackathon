from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser

from .managers import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=200)
    email = models.EmailField(('email address'), unique=True)
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.email} ------------------------ {self.name}'


# this means a company
class Seller(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, help_text="Enter the name of the Company")





    stripe_user_id = models.CharField(max_length=255, blank=True)
    stripe_access_token = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return f'{self.user.email}  ------------------------ {self.user.name}'

# means a hire
class Buyer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, help_text="Enter the name of the Company")

    def __str__(self):
        return  f'{self.user.email}  ------------------------ {self.user.name}'
