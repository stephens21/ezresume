# Generated by Django 2.1.1 on 2018-10-04 23:20

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20181003_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
