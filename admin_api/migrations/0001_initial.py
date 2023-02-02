# Generated by Django 3.2.10 on 2022-03-06 16:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('transfer_date', models.DateTimeField(auto_now_add=True)),
                ('ref', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('cat_name', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=False)),
                ('cat_image', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
                'default_permissions': ['add', 'change', 'delete', 'view'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=500)),
                ('city_state', models.CharField(max_length=500)),
                ('city_countory', models.CharField(max_length=500)),
                ('transdate', models.CharField(max_length=1000)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('transfer_date', models.DateTimeField(auto_now_add=True)),
                ('ref', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('main_cat_name', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=True)),
                ('main_cat_image', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
                'default_permissions': ['add', 'change', 'delete', 'view'],
            },
        ),
        migrations.CreateModel(
            name='MainService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('transfer_date', models.DateTimeField(auto_now_add=True)),
                ('ref', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('main_service_name', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=False)),
                ('main_service_image', models.CharField(max_length=500)),
                ('cat_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.category')),
                ('main_cat_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.maincategory')),
            ],
            options={
                'abstract': False,
                'default_permissions': ['add', 'change', 'delete', 'view'],
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=500)),
                ('partner_image', models.CharField(max_length=500)),
                ('partner_image_url', models.CharField(max_length=500)),
                ('partner_gender', models.CharField(max_length=500)),
                ('partner_email', models.EmailField(max_length=500)),
                ('partner_phone', models.CharField(max_length=1000)),
                ('partner_proffetion', models.CharField(max_length=1000)),
                ('transdate', models.CharField(max_length=1000)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('transfer_date', models.DateTimeField(auto_now_add=True)),
                ('ref', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('service_name', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=False)),
                ('service_image', models.CharField(max_length=500)),
                ('service_charge', models.CharField(max_length=1000)),
                ('service_time', models.CharField(max_length=1000)),
                ('discount', models.CharField(max_length=1000)),
                ('cat_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.category')),
                ('main_cat_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.maincategory')),
                ('main_service_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.mainservice')),
            ],
            options={
                'abstract': False,
                'default_permissions': ['add', 'change', 'delete', 'view'],
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='slider')),
                ('text', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceFAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queestion', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.service')),
            ],
        ),
        migrations.CreateModel(
            name='PartnerWorkBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pwb_image', models.CharField(max_length=255)),
                ('transdate', models.CharField(max_length=1000)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.partner')),
            ],
        ),
        migrations.CreateModel(
            name='PartnerServiceRefrence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refrence_name', models.CharField(max_length=255)),
                ('refrence_dec', models.CharField(max_length=255)),
                ('transdate', models.CharField(max_length=1000)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.partner')),
            ],
        ),
        migrations.CreateModel(
            name='PartnerServiceLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pap_location', models.CharField(max_length=255)),
                ('transdate', models.CharField(max_length=1000)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.partner')),
            ],
        ),
        migrations.CreateModel(
            name='PartnerProffetionalDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_card', models.CharField(max_length=500)),
                ('business_name', models.CharField(max_length=500)),
                ('alternate_mobile', models.CharField(max_length=500)),
                ('alternate_email', models.EmailField(max_length=500)),
                ('proffetinal_experience', models.CharField(max_length=1000)),
                ('type_of_dealer', models.CharField(max_length=1000)),
                ('service_provoided', models.CharField(max_length=1000)),
                ('minimum_warranty', models.CharField(max_length=1000)),
                ('website_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('company_intro', models.CharField(blank=True, max_length=1000, null=True)),
                ('transdate', models.CharField(max_length=1000)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.partner')),
            ],
        ),
        migrations.CreateModel(
            name='PartnerDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=500)),
                ('document_file', models.CharField(max_length=500)),
                ('father_name', models.CharField(max_length=500)),
                ('date_of_birth', models.DateField()),
                ('street_address', models.CharField(max_length=255)),
                ('partner_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.city')),
                ('partner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.partner')),
            ],
        ),
        migrations.CreateModel(
            name='PartnerAwardAndPhote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pap_name', models.CharField(max_length=255)),
                ('pap_image', models.CharField(max_length=255)),
                ('transdate', models.CharField(max_length=1000)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.partner')),
            ],
        ),
        migrations.AddField(
            model_name='partner',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.service'),
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.service')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=500)),
                ('customer_gender', models.CharField(max_length=500)),
                ('customer_email', models.EmailField(max_length=500)),
                ('customer_phone', models.CharField(max_length=1000)),
                ('customer_street', models.CharField(max_length=1000)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.city')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='main_cat_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.maincategory'),
        ),
        migrations.CreateModel(
            name='BookService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookser_date', models.DateField(blank=True, null=True)),
                ('bookser_time', models.TimeField(blank=True, null=True)),
                ('bookser_remark', models.CharField(max_length=255)),
                ('payment_method', models.CharField(max_length=55)),
                ('transdate', models.DateTimeField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.customer')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.service')),
            ],
        ),
        migrations.CreateModel(
            name='AboutService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('transfer_date', models.DateTimeField(auto_now_add=True)),
                ('ref', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=500)),
                ('video', models.CharField(max_length=1000)),
                ('discription', models.CharField(max_length=10000)),
                ('notes', models.CharField(max_length=1000)),
                ('service_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_api.service')),
            ],
            options={
                'abstract': False,
                'default_permissions': ['add', 'change', 'delete', 'view'],
            },
        ),
    ]
