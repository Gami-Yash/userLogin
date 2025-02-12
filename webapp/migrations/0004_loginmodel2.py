# Generated by Django 4.2.7 on 2023-12-28 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_loginmodel_last_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='loginmodel2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
