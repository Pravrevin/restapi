from django.db import models

class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    EffectiveStartDate = models.DateField(default= '')
    EffectiveEndDate = models.DateField(default='')
    state = models.IntegerField(default='')
    status = models.IntegerField(default='')

