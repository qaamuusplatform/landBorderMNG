# Generated by Django 4.2.2 on 2023-07-27 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_fingerprintscandt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fingerprintscandt',
            name='fingerPrintImage',
            field=models.FileField(blank=True, default='fingerprint.jpg', null=True, upload_to='scannedFingers/'),
        ),
    ]
