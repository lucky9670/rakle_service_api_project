# Generated by Django 4.2.3 on 2023-07-18 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_api', '0014_alter_orderacceptance_oredr_status_venderwallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venderwallet',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.orderacceptance', unique=True),
        ),
    ]
