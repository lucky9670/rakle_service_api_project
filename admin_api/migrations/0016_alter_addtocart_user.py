# Generated by Django 3.2.10 on 2023-02-08 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0009_customerdevice'),
        ('admin_api', '0015_auto_20230208_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtocart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer', to='app_login.allcustomer'),
        ),
    ]
