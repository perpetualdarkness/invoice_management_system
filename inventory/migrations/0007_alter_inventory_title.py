# Generated by Django 4.0 on 2022-07-07 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_remove_inventory_id_alter_inventory_product_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='title',
            field=models.CharField(blank=True, default='', max_length=120, unique=True, verbose_name='Title'),
        ),
    ]
