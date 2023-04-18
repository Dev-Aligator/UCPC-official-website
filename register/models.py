from django.db import models
from validator import Validator
from choices import Choices
import uuid

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
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TeamName = models.CharField(max_length=30, null=False, blank=False, unique=True, validators=[Validator.TeamRegex])
    Email = models.EmailField(max_length=30, null=False, blank=False, unique=True)
    FeePayment = models.CharField(max_length=10, null=False, blank=False, choices=Choices.PAYMENT_STATUS_CHOICES, default=Choices.PAYMENT_STATUS_CHOICES[0][0])
    Rank = models.IntegerField(null=False, blank=False, unique=True, default=-1)

    def __str__(self):
        return self.TeamName
    
class User(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Team = models.ForeignKey(Team, on_delete=models.CASCADE)
    Fullname = models.CharField(max_length=30, null=False, blank=False, validators=[Validator.NameRegex])
    MSSV_CMND = models.CharField(max_length=12, null=False, blank=False, unique=True, validators=[Validator.MSSV_CMNDRegex])
    Phone = models.CharField(max_length=11, null=False, blank=False, unique=True, validators=[Validator.PhoneRegex])
    School = models.CharField(max_length=10, null=False, blank=False, choices=Choices.SCHOOL_CHOICES)
    Admin = models.BooleanField(null=False, blank=False, default=False)
    Leader = models.BooleanField(null=False, blank=False, default=False)
    Occupation = models.CharField(max_length=10, null=False, blank=False, choices=Choices.OCCUPATION_CHOICES, default=Choices.OCCUPATION_CHOICES[0][0])
    
    def __str__(self):
        return self.Fullname
    
class Post(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Date = models.DateField(max_length=20, null=False, blank=False)
    Title = models.CharField(max_length=50, null=False, blank=False, unique=True)
    Author = models.CharField(max_length=30, null=False, blank=False, default='Đoàn-Hội Khoa Học Máy Tính UIT')
    Thumbnail = models.URLField(null=False, blank=False, default='https://www.facebook.com/DoanHoiKHMT')
    Post = models.URLField(null=False, blank=False, default='https://www.facebook.com/DoanHoiKHMT')

    def __str__(self):
        return self.Title
    
class Website(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Title = models.CharField(max_length=30, null=False, blank=False)
    Year = models.IntegerField(max_length=4, null=False, blank=False, validators=[Validator.YearRegex])
    Deadline = models.DateTimeField(null=False, blank=False)
    Law = models.JSONField(null=False, blank=False)
    Award = models.JSONField(null=False, blank=False)
    Timeline = models.JSONField(null=False, blank=False)
    Organization = models.JSONField(null=False, blank=False)
    Sponsor = models.JSONField(null=False, blank=False)
    Social = models.JSONField(null=False, blank=False)
    
    def __str__(self):
        return self.Title