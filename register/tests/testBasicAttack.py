from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


from register.models import School, Team

# 👋 TESTING HOMEPAGE

class Home(TestCase):
    def test_able_to_access(self):
        """Check if status is 200 👌"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/home.html')

class UserTest(TestCase):
    def setUp(self):
        user_a = User(username='user',email='user@user.com')
        user_a_pw = '123456'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)
    
    def test_user_password(self):
        user_a = User.objects.get(username='user')
        self.assertTrue(user_a.check_password(self.user_a_pw))
    
    def test_login_url(self):
        login_url = reverse('register:login') 
        data = {"username":"user", "password": self.user_a_pw, "email":"user@user.com"}  
        response = self.client.post(login_url, data, follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)
    
    def test_invalid_request(self):
        self.client.login(username=self.user_a.username, password="invalid_pw")
        response = self.client.post("register/login/",{"title":"this is an valid test"})
        self.assertTrue(response.status_code!=200)

class BaseTestRegister(TestCase):
    def setUp(self):
        self.register_url=reverse('register:register')
        school = School.objects.create(school='Foobar')
        self.user={
            'team': 'Team A',
                'member1': 'Nguyễn Văn Khang',
                'cmnd1': '111111111',
                'phone1': '0111111111',
                'member2': 'Trương Minh Quân',
                'cmnd2': '111111111',
                'phone2': '0111111111',
                'member3': 'Nhạc Phi',
                'cmnd3': '111111111',
                'phone3': '0111111111',
                'email': 'test@gm.uit.edu.vn',
                'school': [school.id],
                'password': 'abcdefghB1@'}
        return super().setUp()
        
class TestRegister(BaseTestRegister):
    def test_can_view_page_correctly(self):
       response=self.client.get(self.register_url)
       self.assertEqual(response.status_code,200)
       self.assertTemplateUsed(response,'register/register.html')

    def test_can_register_user(self):
        response=self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)


# 📝 TESTING REGISTER
class Register(TestCase):
    def test_able_to_access(self):
        """Check if status is 200 👌"""
        response = self.client.get(reverse('register:register'))
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        """Check able to register normaly"""
        team_count = Team.objects.count()
        school = School.objects.create(school='Foobar')
        response = self.client.post(
            reverse('register:register'), {
                'team': 'Team A',
                'member1': 'Nguyễn Văn Khang',
                'cmnd1': '123456789',
                'phone1': '0123456789',
                'member2': 'Trương Minh Quân',
                'cmnd2': '123456789',
                'phone2': '01234567891',
                'member3': 'Nhạc Phi',
                'cmnd3': '123456789',
                'phone3': '01234567891',
                'email': 'test@gm.uit.edu.vn',
                'school': [school.id],
                'password': 'abcdefghB1'})
        self.assertEqual(response.status_code, 302)  # HttpResponseRedirect
        self.assertEqual(Team.objects.count(), team_count + 1)


# 📝 TESTING LOGIN
class BaseTestLogin(TestCase):
    def setUp(self):
        self.login_url=reverse('register:login')
        self.user={
            'username':'testuser',
            'email':'test@test.com',
            'password':'123456',}
        return super().setUp()

class Login(BaseTestLogin):
    def test_can_access_page(self):
        response=self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'login/login.html')

    def test_login_success(self):
        response= self.client.post(self.login_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)


class Profile(TestCase):
    def test_able_to_access(self):
        """Check if status is 200 👌"""
        profile_url=reverse('register:profile')
        response = self.client.get(profile_url)
        self.assertEqual(response.status_code, 302)

class Logout(TestCase):
    def test_able_to_access(self):
        """Check if status is 200 👌"""
        logout_url=reverse('register:logout')
        response = self.client.get(logout_url)
        self.assertEqual(response.status_code, 302)

