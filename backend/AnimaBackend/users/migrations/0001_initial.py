# Generated by Django 3.2.9 on 2021-11-08 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('username', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Username')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('about', models.TextField(blank=True, max_length=5000, null=True)),
                ('birth_date', models.DateField(null=True, verbose_name='Date of birth:')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='City')),
                ('gender', models.CharField(blank=True, choices=[('male', 'm'), ('female', 'fm')], max_length=10, null=True)),
                ('image', models.ImageField(null=True, upload_to='users/images', verbose_name='Image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
