# Generated by Django 4.2.7 on 2023-12-27 19:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_loginmodel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginmodel',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
