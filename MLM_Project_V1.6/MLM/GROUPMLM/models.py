from django.db import models
from MLMAPP.models import MyUser

class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    created_date = models.DateField(default ='')
    EffectiveStartDate = models.DateField(default= '')
    EffectiveEndDate = models.DateField(default='')
    state = models.CharField(max_length=10,default='0')
    g_status = models.CharField(max_length=10,default='0')



class Share(models.Model):
    share_id = models.AutoField(primary_key=True)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    user_id=models.ForeignKey(MyUser, on_delete=models.CASCADE)
    s_status = models.CharField(max_length=10,default='0')