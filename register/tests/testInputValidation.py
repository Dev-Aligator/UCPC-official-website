from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import IntegrityError

from register.models import School, Team


# Testing GET requests

class GetRequestsViewsTests(TestCase):
    
    def test_get_home_view(self):
        response = self.client.get(reverse('register:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/home.html')

    def test_get_register_view(self):
        response = self.client.get(reverse('register:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/register.html')

    def test_get_login_view(self):
        response = self.client.get(reverse('register:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')

    def test_get_profile_view(self):
        profile_url=reverse('register:profile')
        response = self.client.get(profile_url)
        self.assertEqual(response.status_code, 302)
    
    def test_get_logout_view(self):
        logout_url=reverse('register:logout')
        response = self.client.get(logout_url)
        self.assertEqual(response.status_code, 302)

# Testing POST requests

class PostRequestsViewsTests(TestCase):

    # Test valid 
    def test_post_register_valid(self):
        team_count = Team.objects.count()
        school = School.objects.create(school='Foobar')
        response = self.client.post(
            reverse('register:register'), {
                'team': 'Team A',
                'member1': 'Nguyễn Văn Khang',
                'cmnd1': '987654321', # cmnd 9 digits
                'phone1': '0123456789', # phone number 10 digits
                'member2': 'Trương Minh Quân',
                'cmnd2': '987654321000', # cccd 12 digits
                'phone2': '01234567890', # phone number 11 digits
                'member3': 'Nhạc Phi',
                'cmnd3': '987654321000', # cccd 12 digits
                'phone3': '01234567890', # phone number 11 digits
                'email': 'test@gm.uit.edu.vn',
                'school': [school.id],
                'password': 'abcdefB1@'})
        self.assertEqual(response.status_code, 302) # redirect to login
        self.assertEqual(Team.objects.count(), team_count + 1)

    # Test invalid member's name
    def test_post_register_invalid_member_name(self):
        team_count = Team.objects.count()
        school = School.objects.create(school='Foobar')
        response = self.client.post(
            reverse('register:register'), {
                'team': 'Team A',
                'member1': '😁😁😁', # invalid name
                'cmnd1': '987654321', # cmnd 9 digits
                'phone1': '0123456789', # phone number 10 digits
                'member2': '😁😁😁',
                'cmnd2': '987654321000', # cccd 12 digits
                'phone2': '01234567890', # phone number 11 digits
                'member3': '😁😁😁', # invalid name
                'cmnd3': '987654321000', # cccd 12 digits
                'phone3': '01234567890', # phone number 11 digits
                'email': 'test@gm.uit.edu.vn',
                'school': [school.id],
                'password': 'password'})
        self.assertEqual(response.status_code, 422) # render again register.html and show error
        self.assertEqual(Team.objects.count(), team_count)

    # Test invalid team's name
    def test_post_register_invalid_team_name(self):
        team_count = Team.objects.count()
        school = School.objects.create(school='Foobar')
        response = self.client.post(
            reverse('register:register'), {
                'team': '💕💕💕', # invalid team's name
                'member1': 'Nguyễn Văn Khang',
                'cmnd1': '987654321', # cmnd 9 digits
                'phone1': '0123456789', # phone number 10 digits
                'member2': 'Trương Minh Quân',
                'cmnd2': '987654321000', # cccd 12 digits
                'phone2': '01234567890', # phone number 11 digits
                'member3': 'Nhạc Phi',
                'cmnd3': '987654321000', # cccd 12 digits
                'phone3': '01234567890', # phone number 11 digits
                'email': 'test@gm.uit.edu.vn',
                'school': [school.id],
                'password': 'password'})
        self.assertEqual(response.status_code, 422) # render again register.html and show error
        self.assertEqual(Team.objects.count(), team_count)

    # Test invalid email address
    def test_post_register_invalid_email(self):
        team_count = Team.objects.count()
        school = School.objects.create(school='Foobar')
        response = self.client.post(
            reverse('register:register'), {
                'team': 'Team A',
                'member1': 'Nguyễn Văn Khang',
                'cmnd1': '987654321', # cmnd 9 digits
                'phone1': '0123456789', # phone number 10 digits
                'member2': 'Trương Minh Quân',
                'cmnd2': '987654321000', # cccd 12 digits
                'phone2': '01234567890', # phone number 11 digits
                'member3': 'Nhạc Phi',
                'cmnd3': '987654321000', # cccd 12 digits
                'phone3': '01234567890', # phone number 11 digits
                'email': 'test.vn', # invalid email address
                'school': [school.id],
                'password': 'password'})
        self.assertEqual(response.status_code, 422) # render again register.html and show error
        self.assertEqual(Team.objects.count(), team_count)

    # Test invalid phone number
    def test_post_register_invalid_phone(self):
        team_count = Team.objects.count()
        school = School.objects.create(school='Foobar')
        response = self.client.post(
            reverse('register:register'), {
                'team': 'Team A',
                'member1': 'Nguyễn Văn Khang',
                'cmnd1': '987654321',
                'phone1': '0123', # phone number 10 digits (fill 4 digits => fail)
                'member2': 'Trương Minh Quân',
                'cmnd2': '987654321000',
                'phone2': '012345678', # phone number 11 digits (fill 9 digits => fail)
                'member3': 'Nhạc Phi',
                'cmnd3': '987654321000',
                'phone3': '01234567890', # phone number 11 digits (fill 10 or 11 digits => success)
                'email': 'test@gm.uit.edu.vn',
                'school': [school.id],
                'password': 'password'})
        self.assertEqual(response.status_code, 422) # render again register.html and show error
        self.assertEqual(Team.objects.count(), team_count)

    # Test invalid CMND/CCCD
    def test_post_register_invalid_cmnd(self):
        team_count = Team.objects.count()
        school = School.objects.create(school='Foobar')
        response = self.client.post(
            reverse('register:register'), {
                'team': 'Team A',
                'member1': 'Nguyễn Văn Khang',
                'cmnd1': '98765432', # cmnd 9 digits (fill 8 digits => fail)
                'phone1': '0123456789', 
                'member2': 'Trương Minh Quân',
                'cmnd2': '9876543210', # cccd 12 digits (fill 10 digits => fail)
                'phone2': '01234567890',
                'member3': 'Nhạc Phi',
                'cmnd3': '987654321000', # cccd 12 digits (fill 11 digits => fail)
                'phone3': '01234567890', 
                'email': 'test@gm.uit.edu.vn',
                'school': [school.id],
                'password': 'password'})
        self.assertEqual(response.status_code, 422) # render again register.html and show error
        self.assertEqual(Team.objects.count(), team_count)

    # Test valid CMND/CCCD
    def test_post_register_valid_cmnd(self):
        team_count = Team.objects.count()
        school = School.objects.create(school='Foobar')
        response = self.client.post(
            reverse('register:register'), {
                'team': 'Team A',
                'member1': 'Nguyễn Văn Khang',
                'cmnd1': '987654321', # cmnd 9 digits
                'phone1': '0123456789', 
                'member2': 'Trương Minh Quân',
                'cmnd2': '987654321000', # cccd 12 digits
                'phone2': '01234567890',
                'member3': 'Nhạc Phi',
                'cmnd3': '987654321', # cccd 9 digits
                'phone3': '01234567890', 
                'email': 'test@gm.uit.edu.vn',
                'school': [school.id],
                'password': 'abcdefgB01@'})
        self.assertEqual(response.status_code, 302) # render again register.html and show error
        self.assertEqual(Team.objects.count(), team_count+1)

    # Test XSS 
    def test_post_register_XSS(self):
        team_count = Team.objects.count()
        school = School.objects.create(school='Foobar')
        response = self.client.post(
            reverse('register:register'), {
                'team': "<script>alert('hello')</script>",
                'member1': "<script>alert('hello')</script>",
                'cmnd1': '123456',
                'phone1': '0983416237',
                'member2': "<script>alert('hello')</script>",
                'cmnd2': '123456',
                'phone2': '0983416237',
                'member3': "<script>alert('hello')</script>",
                'cmnd3': '123456',
                'phone3': '0983416237',
                'email': 'test@gm.uit.edu.vn',
                'school': [school.id],
                'password': 'password'})
        self.assertEqual(response.status_code, 422) # render again register.html and show error
        self.assertEqual(Team.objects.count(), team_count)

    # Test SQL Injection
    def test_post_register_sql_injection(self):
        team_count = Team.objects.count()
        school = School.objects.create(school='Foobar')
        response = self.client.post(
            reverse('register:register'), {
                'team': 'SELECT * FROM Team',
                'member1': 'SELECT * FROM Team',
                'cmnd1': '123456',
                'phone1': '0983416237',
                'member2': 'SELECT * FROM Team',
                'cmnd2': '123456',
                'phone2': '0983416237',
                'member3': 'SELECT * FROM Team',
                'cmnd3': '123456',
                'phone3': '0983416237',
                'email': 'test@gm.uit.edu.vn',
                'school': [school.id],
                'password': 'password'})
        self.assertEqual(response.status_code, 422) # render again register.html and show error
        self.assertEqual(Team.objects.count(), team_count)
    
    # Test Login
    def setUp(self):
        self.login_url=reverse('register:login')
        self.user={
            'username':'testuser',
            'email':'test@test.com',
            'password':'123456',}
        return super().setUp()

    def test_post_login_valid(self):
        response= self.client.post(self.login_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302) #redirect to profile

    def test_post_login_invalid(self):
        response= self.client.post(self.login_url,{'username':'testuser','email':'test@test.com','password':'wrongpass'},format='text/html')
        self.assertEqual(response.status_code,302) # redirect to login and show error

# Testing School Models
class SchoolModelTests(TestCase):

    def test_school_string_representation(self):
        school_a = School(
            school="DH Quoc Te",
            logo_path = "images/quocte.png"
        )
        expected='DH Quoc Te'
        self.assertEqual(str(school_a),expected)



    
    