# Generated by Django 2.2 on 2020-01-07 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MLMAPP', '0005_auto_20200107_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(default='RIJMZB', max_length=6, unique=True),
        ),
    ]