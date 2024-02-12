from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .manager import CustomUserManager
from uuid import uuid4
import os

transaction_status_choices=(("Success","Success"),
                 ("In Progress","In Progress"),
                 ("On Hold","On Hold"),
                 ("Failed","Failed"),
                 ("Pending","Pending"),
                 ("Aborted","Aborted"),
                 ("Unconfirmed","Unconfirmed"),
                 ("Cancelled","Cancelled")
                 )

sale_choices=(("Local_Hotel","Inventory Hotel"),
                 ("TripJack_Hotel","TripJack Hotel"),
                 ("Local_Flights","Inventory Flights"),
                 ("TripJack_Flights","TripJack Flights"),
                 )


class CustomUser(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(('email address main'), unique=True)
    first_name = models.CharField(('first name'), max_length=130, null=True,blank=True)
    last_name = models.CharField(('last name'), max_length=150, null=True ,blank=True)
    contact_no = models.BigIntegerField(('contact no'), blank=True, null=True)
    date_joined = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_Teacher = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)
    
    def save(self, *args, **kwargs):
        # Set balance only if the user is an agent and balance is provided
        

        super().save(*args, **kwargs)

    @property
    def id(self):
        return int(self.pk)



    
    
    # Add fields specific to agents
    # Add more agent-specific fields here




class Transection(models.Model):
    From = models.EmailField((""), max_length=254) 
    To = models.CharField( max_length=50,default='')
    Transaction_id = models.CharField(
        max_length=10000, default='')
    Transaction_date = models.DateTimeField(auto_now=True)
    Transaction_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Transaction_status =  models.CharField(choices=transaction_status_choices,max_length=255, null=True, blank=True)
    Transaction_remark = models.CharField(max_length=200, default='')
    Transaction_type = models.CharField(max_length=200, default='')

class Journal(models.Model):
    From = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="From_Account")
    To = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="To_Account")
    Transaction_id = models.CharField(max_length=256, default='',unique=True,null=False)
    agent_balance = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    Transaction_date = models.DateTimeField(auto_now=True)
    Transaction_amount = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    Transaction_status =  models.CharField(choices=transaction_status_choices,max_length=255, null=True, blank=True)
    Transaction_remark = models.CharField(max_length=200, default='')
    
    


class sale(models.Model):
    agent_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="agent_user")
    Transaction_id = models.CharField(max_length=256, default='',unique=True,null=False)
    Transaction_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    commision =  models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    Transaction_status =  models.CharField(choices=transaction_status_choices,max_length=255, null=True, blank=True)
    sale_type = models.CharField(choices=sale_choices,max_length=255, null=True, blank=True)
    Cancelled = models.BooleanField(default=False)

