from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import UserManager

BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
]

# DOCUMENT_CHOICES = [
#     ('passport', 'Passport'),
#     ('driving license', 'Driving License'),
#     ('national identification card', 'National Identification Card'),
#     ('residence permit', 'Residence Permit'),
#     ('other', 'Other'),  # Add more choices as needed. For example, 'passport', 'driving license', 'national identification card', 'residence permit', 'other'
# ]

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True, help_text= "Enter the date formate year-month-day")
    gender = models.CharField(max_length=255, choices=[{'male': 'Male', 'female': 'Female'}])
    blood_group = models.CharField(max_length=3, null= True, blank= True, choices=BLOOD_GROUP_CHOICES)
    # identity_document_type = models.CharField(max_length=32, choices=DOCUMENT_CHOICES, blank=True, null= True)
    # identity_document_number = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='images/profileImage/', null=True)
    date_joined = models.DateField(default=timezone.now)
    last_update = models.DateField(auto_now = True)
    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
    objects = UserManager()