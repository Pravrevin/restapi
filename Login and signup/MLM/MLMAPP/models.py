from django.db import models


class RegistrationDetails(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100,default='')
    password = models.CharField(max_length=100)
    mobilenumber = models.CharField(max_length=100)
    refercode = models.CharField(max_length=100)

    def __str__(self):
        return self.username
