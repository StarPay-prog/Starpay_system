from django.db import models
from django.contrib.sessions.models import Session

    
    
class CustomSession(models.Model):
    session = models.ForeignKey(Session,unique = False, on_delete=models.CASCADE)
    IP = models.CharField(max_length=100)    
    user = models.CharField(max_length= 100)
    USER_TYPES = [
        ('admin', 'admin'),
        ('super_admin', 'super admin'),
        ('merchant', 'merchant'),
    ]
    
    user_type = models.CharField(max_length=32, choices=USER_TYPES)


