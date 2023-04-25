# Generated by Django 3.2.13 on 2022-05-11 06:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20220428_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='mssv1',
            field=models.CharField(max_length=20, null=True, unique=True, validators=[django.core.validators.RegexValidator('^([0-9])$')]),
        ),
        migrations.AddField(
            model_name='team',
            name='mssv2',
            field=models.CharField(max_length=20, null=True, unique=True, validators=[django.core.validators.RegexValidator('^([0-9])$')]),
        ),
        migrations.AddField(
            model_name='team',
            name='mssv3',
            field=models.CharField(max_length=20, null=True, unique=True, validators=[django.core.validators.RegexValidator('^([0-9])$')]),
        ),
        migrations.AlterField(
            model_name='team',
            name='cmnd1',
            field=models.CharField(max_length=12, null=True, unique=True, validators=[django.core.validators.RegexValidator('^([0-9]|[0-9]{12})$')]),
        ),
        migrations.AlterField(
            model_name='team',
            name='cmnd2',
            field=models.CharField(max_length=12, null=True, unique=True, validators=[django.core.validators.RegexValidator('^([0-9]|[0-9]{12})$')]),
        ),
        migrations.AlterField(
            model_name='team',
            name='cmnd3',
            field=models.CharField(max_length=12, null=True, unique=True, validators=[django.core.validators.RegexValidator('^([0-9]|[0-9]{12})$')]),
        ),
    ]