# Generated by Django 4.2.2 on 2023-07-04 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landApp', '0007_reportinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='borderregistration',
            name='fromCountry',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='borderregistration',
            name='passportId',
            field=models.CharField(default='', max_length=266),
        ),
        migrations.AddField(
            model_name='borderregistration',
            name='porderGeneratedId',
            field=models.CharField(default='borderId_3074', max_length=255),
        ),
    ]
