# Generated by Django 3.2.10 on 2023-02-04 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_api', '0011_alter_category_cat_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainservice',
            name='main_service_image',
            field=models.ImageField(upload_to='main_service'),
        ),
    ]
