# Generated by Django 3.2.10 on 2022-03-26 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_api', '0002_videoconsultation'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('offerimage', models.FileField(upload_to='offer')),
                ('offer', models.CharField(max_length=100)),
            ],
        ),
    ]
