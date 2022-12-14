# Generated by Django 4.0 on 2022-08-06 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(blank=True, default='', max_length=75, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Customer ID'),
        ),
    ]
