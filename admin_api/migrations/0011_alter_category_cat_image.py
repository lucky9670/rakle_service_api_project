# Generated by Django 3.2.10 on 2023-02-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_api', '0010_auto_20230204_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(upload_to='category'),
        ),
    ]
