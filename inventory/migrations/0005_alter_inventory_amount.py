# Generated by Django 4.0 on 2022-07-05 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_inventory_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='amount',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price'),
        ),
    ]
