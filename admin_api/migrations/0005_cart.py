# Generated by Django 3.2.10 on 2023-02-12 16:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0001_initial'),
        ('admin_api', '0004_auto_20230212_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('transfer_date', models.DateTimeField(auto_now_add=True)),
                ('ref', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_login.allcustomer')),
            ],
            options={
                'abstract': False,
                'default_permissions': ['add', 'change', 'delete', 'view'],
            },
        ),
    ]
