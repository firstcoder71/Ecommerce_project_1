# Generated by Django 4.2.5 on 2023-12-09 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_alter_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='zipcode',
            field=models.IntegerField(default=1),
        ),
    ]
