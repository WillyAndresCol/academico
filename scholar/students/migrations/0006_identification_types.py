# Generated by Django 4.2.6 on 2023-11-08 00:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_user_update_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Identification_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abrev', models.CharField(max_length=10)),
                ('descrip', models.CharField(max_length=100)),
                ('create_at', models.DateTimeField(default=datetime.datetime.now)),
                ('update_at', models.DateTimeField(default=datetime.datetime.now)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
    ]
