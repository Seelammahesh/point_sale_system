# Generated by Django 4.2.4 on 2023-09-19 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datarepo', '0008_rename_created_on_product_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
