# Generated by Django 2.2 on 2020-01-13 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('AdharCard', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Pancard', models.CharField(default='', max_length=30)),
                ('AltMobileNumber', models.CharField(default='', max_length=30)),
                ('image', models.ImageField(default='', max_length=255, null=True, upload_to='Images/')),
                ('number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
