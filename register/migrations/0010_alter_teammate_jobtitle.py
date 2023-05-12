# Generated by Django 3.2.13 on 2023-05-11 07:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_alter_teammate_cmnd_cccd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammate',
            name='JobTitle',
            field=models.CharField(default='Pupil/Student', max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂẾưăạảấầẩẫậắằẳẵặẹẻẽềềểếỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳýỵỷỹ\\s\\W|_]+$')]),
        ),
    ]