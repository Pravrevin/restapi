# Generated by Django 2.2 on 2020-01-14 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MLMAPP', '0003_auto_20200114_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(default='AHLBH9', max_length=6, unique=True),
        ),
    ]
