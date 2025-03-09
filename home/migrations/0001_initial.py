# Generated by Django 4.1.13 on 2025-03-08 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='discount_percentage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('percent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'discount_percentage',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('description2', models.TextField()),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_discount_percentage', models.ForeignKey(db_column='id_discount_percentage', on_delete=django.db.models.deletion.CASCADE, related_name='discount_percentage', to='home.discount_percentage')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='UserClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('password', models.CharField(max_length=255)),
                ('auth_type', models.CharField(choices=[('email', 'Email'), ('facebook', 'Facebook'), ('tranditional', 'Tranditional')], max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('last_login', models.DateField(blank=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Productvariant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('size', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='products/%Y/%m/%d')),
                ('stock', models.IntegerField(max_length=11)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='home.product')),
            ],
            options={
                'db_table': 'productvariant',
            },
        ),
        migrations.CreateModel(
            name='Producttype',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('category_id', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
            options={
                'db_table': 'producttype',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(db_column='type', on_delete=django.db.models.deletion.CASCADE, to='home.producttype'),
        ),
    ]
