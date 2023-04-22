from django.db import models
<<<<<<< HEAD
from .validator import Validator
from .choices import Choices
import uuid
=======
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
TeamRegex = RegexValidator(r'(\b\S*[AĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴA-Z]+\S*\b){1,}')
NameRegex = RegexValidator(r'^[a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂẾưăạảấầẩẫậắằẳẵặẹẻẽềềểếỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳýỵỷỹ\s\W|_]+$')
NumberRegex = RegexValidator(r'^([0-9]{10}|[0-9]{11})$')
CMNDandCCCD = RegexValidator(r'^([0-9]{9}|[0-9]{12})$')
MSSVRegex = RegexValidator(r'^[a-zA-Z0-9]+$')
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

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UcpcUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class UcpcUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UcpcUserManager()
>>>>>>> remotes/origin/login-register

class Team(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TeamName = models.CharField(max_length=30, null=False, blank=False, unique=True, validators=[Validator.TeamRegex])
    Email = models.EmailField(null=False, blank=False, unique=True)
    FeePayment = models.CharField(max_length=10, null=False, blank=False, choices=Choices.PAYMENT_STATUS_CHOICES, default=Choices.PAYMENT_STATUS_CHOICES[0][0])
    Rank = models.IntegerField(null=False, blank=False, unique=True, default=-1)

    def __str__(self):
<<<<<<< HEAD
        return self.TeamName
    
class Teammate(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Team = models.ForeignKey(Team, on_delete=models.CASCADE)
    Fullname = models.CharField(max_length=30, null=False, blank=False, validators=[Validator.NameRegex])
    MSSV_CMND = models.CharField(max_length=12, null=False, blank=False, unique=True, validators=[Validator.MSSV_CMNDRegex])
    Phone = models.CharField(max_length=11, null=False, blank=False, unique=True, validators=[Validator.PhoneRegex])
    School = models.CharField(max_length=10, null=False, blank=False, choices=Choices.SCHOOL_CHOICES)
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
    Year = models.IntegerField(null=False, blank=False, validators=[Validator.YearRegex])
    Deadline = models.DateTimeField(null=False, blank=False)
    Law = models.JSONField(null=False, blank=False)
    Award = models.JSONField(null=False, blank=False)
    Timeline = models.JSONField(null=False, blank=False)
    Organization = models.JSONField(null=False, blank=False)
    Sponsor = models.JSONField(null=False, blank=False)
    Social = models.JSONField(null=False, blank=False)
    
    def __str__(self):
        return self.Title
=======
        return self.team
    

>>>>>>> remotes/origin/login-register
