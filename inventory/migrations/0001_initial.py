# Generated by Django 4.0.4 on 2022-07-04 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.TextField(blank=True, default='', max_length=3000, null=True)),
                ('title', models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Title')),
                ('amount', models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price')),
            ],
        ),
    ]
