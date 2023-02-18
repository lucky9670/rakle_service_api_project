# Generated by Django 3.2.10 on 2023-02-12 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0001_initial'),
        ('admin_api', '0006_auto_20230212_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='user_device_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_login.customerdevice'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_login.allcustomer'),
        ),
    ]
