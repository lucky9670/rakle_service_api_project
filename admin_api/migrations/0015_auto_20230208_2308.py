# Generated by Django 3.2.10 on 2023-02-08 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_login', '0009_customerdevice'),
        ('admin_api', '0014_auto_20230204_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtocart',
            name='user_device_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_device', to='app_login.customerdevice'),
        ),
        migrations.AlterField(
            model_name='addtocart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
    ]
