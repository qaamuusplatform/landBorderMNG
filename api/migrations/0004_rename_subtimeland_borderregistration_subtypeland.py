# Generated by Django 4.2.2 on 2023-08-15 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_borderregistration_subtimeland'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borderregistration',
            old_name='subTimeLand',
            new_name='subTypeLand',
        ),
    ]
