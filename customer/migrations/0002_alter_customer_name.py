# Generated by Django 4.0 on 2022-07-17 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.TextField(blank=True, default='', max_length=50, null=True),
        ),
    ]