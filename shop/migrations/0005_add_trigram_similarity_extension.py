from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('shop','0004_alter_product_title'),
    ]

    operations = [TrigramExtension()]  