from django.db import models

from apps.users.models import Seller
from autoslug import AutoSlugField


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    #slug = models.SlugField(max_length=255)
    slug =  AutoSlugField(populate_from='title', unique=True, max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    fee = models.PositiveIntegerField(default=50)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

# RECOMMENDATION
from apps.users.models import Seller as Company

# Create your models here.
class Company_Profile(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    INDUSTRY_CHOICES = [
        ('Software Development & IT Services', 'Renewable Energy'),
        # Add more industry choices if needed
    ]
 
    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES, default='Software Development & IT Services')
    location = models.CharField(max_length=255, default='San Francisco, California, USA')
    founded = models.DateField(default=2007)
    employees = models.CharField(max_length=20, default='500-1000')
    ceo = models.CharField(max_length=100, default='Jane Smith')
    description = models.TextField()
 
    def __str__(self):
        return f"{self.industry} - {self.location}" 
    

class Job_Description(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, help_text="Enter the job role")
    job_description = models.TextField()
 
    responsibilities = models.TextField()
    requirements = models.TextField()
 
    def __str__(self):
        return self.role
    


class Meeting(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
 
    title = models.CharField(max_length=100, help_text="Enter the meeting title")
    attendees = models.TextField()
    agenda = models.TextField()
 
    def __str__(self):
        return self.title
    

class Project_Documentation(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, help_text="Enter the project title")
    introduction = models.TextField()
    project_overview = models.TextField()
    technologies_in_use = models.TextField()
    project_scope_in_scope = models.TextField()
    project_scope_out_of_scope = models.TextField()
    stakeholders = models.TextField()
    project_timeline = models.TextField()
    project_deliverables = models.TextField()
    risk_management = models.TextField()
    conclusion = models.TextField()
    appendices = models.TextField()
 
    def __str__(self):
        return self.title
