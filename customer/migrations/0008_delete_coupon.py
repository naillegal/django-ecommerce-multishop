# Generated by Django 4.2.2 on 2023-08-09 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_alter_coupon_used_customers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coupon',
        ),
    ]