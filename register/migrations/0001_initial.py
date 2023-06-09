# Generated by Django 3.2.13 on 2023-04-24 08:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UcpcUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Date', models.DateField(max_length=20)),
                ('Title', models.CharField(max_length=50, unique=True)),
                ('Author', models.CharField(default='Đoàn-Hội Khoa Học Máy Tính UIT', max_length=30)),
                ('Thumbnail', models.URLField(default='https://www.facebook.com/DoanHoiKHMT')),
                ('Post', models.URLField(default='https://www.facebook.com/DoanHoiKHMT')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('TeamName', models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator('(\\b\\S*[AĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴA-Z]+\\S*\\b){1,}')])),
                ('FeePayment', models.CharField(choices=[('PEND', 'Pending'), ('CMPL', 'Completed'), ('FAIL', 'Failed')], default='PEND', max_length=10)),
                ('Rank', models.IntegerField(default=-1, unique=True)),
                ('UcpcUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=30)),
                ('Year', models.IntegerField(validators=[django.core.validators.RegexValidator('^\\d{4}$')])),
                ('Deadline', models.DateTimeField()),
                ('Law', models.JSONField()),
                ('Award', models.JSONField()),
                ('Timeline', models.JSONField()),
                ('Organization', models.JSONField()),
                ('Sponsor', models.JSONField()),
                ('Social', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Teammate',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Fullname', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂẾưăạảấầẩẫậắằẳẵặẹẻẽềềểếỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳýỵỷỹ\\s\\W|_]+$')])),
                ('MSSV_CMND', models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator('^([0-9]{8}|[0-9]{9}|[0-9]{12})$')])),
                ('Phone', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('(84|0[3|5|7|8|9])+([0-9]{8})\\b')])),
                ('School', models.CharField(choices=[('UIT', 'Đại học Công nghệ Thông tin - Đại học quốc gia thành phố Hồ Chí Minh')], max_length=10)),
                ('Leader', models.BooleanField(default=False)),
                ('Occupation', models.CharField(choices=[('ST', 'Student'), ('PP', 'Pupil'), ('TC', 'Teacher')], default='ST', max_length=10)),
                ('Team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.team')),
            ],
        ),
    ]
