# Generated by Django 4.2.5 on 2023-12-24 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0007_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='district',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='division',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='thana',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='villorroad',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='customer',
            name='address_line_1',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='address_line_2',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='area',
            field=models.CharField(blank=True, choices=[('', 'Choose Your Division'), ('Dhaka', 'Dhaka'), ('Rangpur', 'Rangpur'), ('Rajshahi', 'Rajshahi'), ('Khulna', 'Khulna'), ('Barishal', 'Barishal'), ('Chattogram', 'Chattogram'), ('Mymenshing', 'Mymenshing'), ('Sylhet', 'Sylhet')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='mobile_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='postcode',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='region',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='surname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
