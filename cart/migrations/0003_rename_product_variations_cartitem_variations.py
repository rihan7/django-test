# Generated by Django 3.2.3 on 2022-02-12 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cartitem_product_variations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='product_variations',
            new_name='variations',
        ),
    ]
