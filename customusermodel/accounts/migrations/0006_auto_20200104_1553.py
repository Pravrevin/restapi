# Generated by Django 2.2 on 2020-01-04 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200104_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='number',
            field=models.CharField(max_length=100),
        ),
    ]
