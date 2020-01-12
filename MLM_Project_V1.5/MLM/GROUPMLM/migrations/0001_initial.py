# Generated by Django 2.2 on 2020-01-12 11:20

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
            name='Group',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateField(default='')),
                ('EffectiveStartDate', models.DateField(default='')),
                ('EffectiveEndDate', models.DateField(default='')),
                ('state', models.CharField(default='0', max_length=10)),
                ('g_status', models.CharField(default='0', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('share_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('s_status', models.CharField(default='0', max_length=10)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GROUPMLM.Group')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
