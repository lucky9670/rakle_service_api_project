# Generated by Django 3.2.10 on 2022-04-08 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_api', '0005_userreview_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('review_rating', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=150)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.service')),
            ],
            options={
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='AddToCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=500)),
                ('service_amount', models.CharField(max_length=100)),
                ('service_image', models.CharField(max_length=100)),
                ('service_quantity', models.CharField(max_length=100)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.service')),
            ],
        ),
    ]
