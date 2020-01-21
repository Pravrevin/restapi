from django.db import models
from MLMAPP.models import MyUser
from django.utils import timezone

class MmlTicket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    Issue = models.CharField(max_length=200,default='')
    Description = models.CharField(max_length=200,default ='')
    RequestedDate = models.DateField(default=timezone.now)
    status = models.CharField(max_length=50,default='In Progress')
    Remarks = models.CharField(max_length=100,default='')
    number = models.ForeignKey(MyUser, on_delete=models.CASCADE)
