# Generated by Django 2.2 on 2020-01-04 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_myuser_mobilenumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='mobilenumber',
            new_name='number',
        ),
    ]
