# Generated by Django 4.2.3 on 2023-07-18 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0003_allcustomer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venderprofile',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]
