# Generated by Django 3.2.10 on 2023-02-12 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_api', '0005_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addtocart',
            name='status',
        ),
        migrations.AddField(
            model_name='addtocart',
            name='cart',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='admin_api.cart'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addtocart',
            name='checkouted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='addtocart',
            name='service_amount',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]