# Generated by Django 4.2.2 on 2023-07-22 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_userprofile_password_alter_userprofile_theuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]