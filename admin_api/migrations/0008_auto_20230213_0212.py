# Generated by Django 3.2.10 on 2023-02-12 20:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admin_api', '0007_auto_20230212_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='service_quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='services',
        ),
        migrations.AddField(
            model_name='order',
            name='cart_detail',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='admin_api.addtocart'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
