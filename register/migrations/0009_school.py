# Generated by Django 3.2.13 on 2023-04-12 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_auto_20220512_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('school', models.CharField(max_length=50)),
            ],
        ),
    ]