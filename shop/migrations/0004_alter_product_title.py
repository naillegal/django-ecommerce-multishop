# Generated by Django 4.2.2 on 2023-08-14 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_general'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.TextField(max_length=50),
        ),
    ]
