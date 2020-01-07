from django.db import models
from MLMAPP.models import MyUser

class Profile(models.Model):
    email = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, default='', )
    last_name = models.CharField(max_length=30, default='', )
    AdharCard = models.CharField(max_length=30, default='', )
    Pancard = models.CharField(max_length=30, default='', )
    AltMobileNumber = models.CharField(max_length=30, default='', )
    image = models.ImageField(upload_to='Images/', null=True, max_length=255, default='default.jpg')
