# Generated by Django 4.2.3 on 2023-07-18 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1200)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='products')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_menu', to='products.menu')),
            ],
        ),
    ]
