# Generated by Django 2.2 on 2020-01-20 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MLMAPP', '0004_auto_20200114_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(default='QG5MFU', max_length=6, unique=True),
        ),
    ]