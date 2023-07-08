# Generated by Django 3.2.10 on 2023-02-12 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_api', '0002_auto_20230211_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtocart',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_service', to='admin_api.service'),
        ),
    ]