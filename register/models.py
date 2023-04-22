from django.db import models
from .validator import Validator
from .choices import Choices
import uuid

class Team(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TeamName = models.CharField(max_length=30, null=False, blank=False, unique=True, validators=[Validator.TeamRegex])
    Email = models.EmailField(null=False, blank=False, unique=True)
    FeePayment = models.CharField(max_length=10, null=False, blank=False, choices=Choices.PAYMENT_STATUS_CHOICES, default=Choices.PAYMENT_STATUS_CHOICES[0][0])
    Rank = models.IntegerField(null=False, blank=False, unique=True, default=-1)

    def __str__(self):
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
