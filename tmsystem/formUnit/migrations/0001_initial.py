# Generated by Django 5.1.3 on 2024-11-20 19:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserPos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=32)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='formUnit.userpos')),
            ],
        ),
    ]
