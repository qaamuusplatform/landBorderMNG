# Generated by Django 4.2.2 on 2023-08-06 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_userprofile_fingerprintcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='borderregistration',
            name='borderCurrentState',
            field=models.CharField(choices=[('in', 'In The Country Flight'), ('out', 'Out The Country')], default='in', max_length=255),
        ),
        migrations.AddField(
            model_name='borderregistration',
            name='passportID',
            field=models.CharField(default='PSS-D12', max_length=255),
        ),
        migrations.AddField(
            model_name='borderregistration',
            name='userLandedType',
            field=models.CharField(choices=[('flight', 'By Flight'), ('train', 'By Train'), ('bus', 'By Bus')], default='flight', max_length=255),
        ),
        migrations.AlterField(
            model_name='borderregistration',
            name='nationality',
            field=models.CharField(choices=[('somalia', 'Somalia'), ('somali-land', 'Somali-Land')], default='somalia', max_length=255),
        ),
    ]