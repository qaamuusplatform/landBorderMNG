# Generated by Django 4.1.2 on 2023-05-15 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=255)),
                ('profileImage', models.ImageField(upload_to='borderImages/')),
                ('userType', models.CharField(default='Normal User', max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BorderRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCardNo', models.CharField(max_length=255)),
                ('expireDate', models.DateTimeField(blank=True, null=True)),
                ('userState', models.CharField(max_length=255)),
                ('userAddress', models.CharField(max_length=555)),
                ('enteringDate', models.DateTimeField()),
                ('nationality', models.CharField(max_length=255)),
                ('fingerPrintCD', models.CharField(default='', max_length=10000)),
                ('registrationDate', models.DateTimeField(auto_now=True)),
                ('remainTime', models.DateTimeField(blank=True, null=True)),
                ('products', models.ManyToManyField(to='landApp.product')),
                ('theUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landApp.userprofile')),
            ],
        ),
    ]
