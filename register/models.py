from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import uuid

TeamRegex = RegexValidator(r'(\b\S*[AĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴA-Z]+\S*\b){1,}')
NameRegex = RegexValidator(r'^[a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂẾưăạảấầẩẫậắằẳẵặẹẻẽềềểếỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳýỵỷỹ\s\W|_]+$')
NumberRegex = RegexValidator(r'^([0-9]{10}|[0-9]{11})$')
CMNDandCCCD = RegexValidator(r'^([0-9]{9}|[0-9]{12})$')
MSSVRegex = RegexValidator(r'^[a-zA-Z0-9]+$')
PhoneRegex = RegexValidator(r'(84|0[3|5|7|8|9])+([0-9]{8})\b')
# NameRegex = RegexValidator(
#     r'^([a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂẾưăạảấầẩẫậắằẳẵặẹẻẽềềểếỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ]{1,}\s{0,}){2,7}$'
# )

# Create your models here.
# class School(models.Model):
#     id = models.AutoField(primary_key=True)
#     school = models.CharField(max_length=50, null=False, blank=False)
#     logo_path = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.school

# class Team(models.Model):
#     id = models.AutoField(primary_key=True)
#     team = models.CharField(max_length=30, null=False, blank=False, unique=True, validators=[TeamRegex])

#     member1 = models.CharField(max_length=30, null=False, blank=False, validators=[NameRegex])
#     mssv1 = models.CharField(max_length=30, unique=True, null=True, blank=False, validators=[MSSVRegex])
#     cmnd1 = models.CharField(max_length=12, unique=True, null=True, blank=False, validators=[CMNDandCCCD])
#     phone1 = models.CharField(max_length=11, null=True, blank=False, validators=[NumberRegex])
#     school1 = models.CharField(max_length=100, null=True, blank=False)

#     member2 = models.CharField(max_length=30, null=False, blank=False, validators=[NameRegex])
#     mssv2 = models.CharField(max_length=30, unique=True, null=True, blank=False, validators=[MSSVRegex])
#     cmnd2 = models.CharField(max_length=12, unique=True, null=True, blank=False, validators=[CMNDandCCCD])
#     phone2 = models.CharField(max_length=11, null=True, blank=False, validators=[NumberRegex])
#     school2 = models.CharField(max_length=100, null=True, blank=False)

#     member3 = models.CharField(max_length=30, null=False, blank=False, validators=[NameRegex])
#     mssv3 = models.CharField(max_length=30, unique=True, null=True, blank=False, validators=[MSSVRegex])
#     cmnd3 = models.CharField(max_length=12, unique=True, null=True, blank=False, validators=[CMNDandCCCD])
#     phone3 = models.CharField(max_length=11, null=True, blank=False, validators=[NumberRegex])
#     school3 = models.CharField(max_length=100, null=True, blank=False)

#     email = models.EmailField(null=False, blank=False, unique=True)
#     paid = models.BooleanField(default=False)

#     def __str__(self):
#         return self.team

class Team(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('PEND', 'Pending'),
        ('CMPL', 'Completed'),
        ('FAIL', 'Failed')
    ]
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TeamName = models.CharField(max_length=30, null=False, blank=False, unique=True, validators=[TeamRegex])
    Teammate1ID = models.UUIDField(null=False, blank=False, unique=True, editable=True)
    Teammate2ID = models.UUIDField(null=False, blank=False, unique=True, editable=True)
    Teammate3ID = models.UUIDField(null=False, blank=False, unique=True, editable=True)
    FeePayment = models.CharField(max_length=10, null=False, blank=False, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_CHOICES[0][0])
    Rank = models.IntegerField(null=False, blank=False, unique=True, validators=[NumberRegex])

    
class User(models.Model):
    SCHOOL_CHOICES = [
    ]
    OCCUPATION_CHOICES = [
        ('ST', 'Student'),
        ('PP', 'Pupil')
    ]
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Fullname = models.CharField(max_length=30, null=False, blank=False, validators=[NameRegex])
    Age = models.IntegerField(null=False, blank=False, validators=[NumberRegex])
    Occupation = models.CharField(max_length=10, null=False, blank=False, choices=OCCUPATION_CHOICES, default=OCCUPATION_CHOICES[0][0])
    School = models.CharField(max_length=10, null=False, blank=False, choices=SCHOOL_CHOICES, default=SCHOOL_CHOICES[0][0])
    MSSV = models.CharField(max_length=30, null=True, blank=True, default='', unique=True, validators=[MSSVRegex])
    CMND = models.CharField(max_length=12, null=False, blank=False, unique=True, validators=[CMNDandCCCD])
    Phone = models.CharField(max_length=30, null=False, blank=False, unique=True, validators=[PhoneRegex])
    Email = models.EmailField(max_length=30, null=False, blank=False, unique=True)
    Admin = models.BooleanField(null=False, blank=False, default=False)
    Team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
class Post(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Date = models.DateField(max_length=20, null=False, blank=False)
    Author = models.CharField(max_length=30, null=False, blank=False, default='Đoàn-Hội Khoa Học Máy Tính UIT')
    Thumbnail = models.URLField(null=False, blank=False, default='https://www.facebook.com/DoanHoiKHMT')
    Post = models.URLField(null=False, blank=False, default='https://www.facebook.com/DoanHoiKHMT')