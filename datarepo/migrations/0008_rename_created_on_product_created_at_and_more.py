# Generated by Django 4.2.4 on 2023-08-24 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datarepo', '0007_alter_product_updated_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='updated_on',
            new_name='updated_at',
        ),
    ]