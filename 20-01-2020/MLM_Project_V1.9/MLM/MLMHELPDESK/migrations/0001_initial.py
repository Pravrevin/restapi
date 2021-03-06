# Generated by Django 2.2 on 2020-01-14 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MmlTicket',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('Issue', models.CharField(max_length=200)),
                ('Description', models.CharField(default='', max_length=200)),
                ('RequestedDate', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(default='In Progress', max_length=50)),
                ('Remarks', models.CharField(default='', max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
