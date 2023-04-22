from django.shortcuts import render, redirect
<<<<<<< HEAD
from .forms import TeamForm, LoginForm, HighSchoolFormSet, UniversityFormSet
=======
from .forms import teamForm, loginForm, userForm
>>>>>>> remotes/origin/login-register
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from register.models import Team, Teammate, Post, Website
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from .choices import Choices
=======
from .models import UcpcUser
>>>>>>> remotes/origin/login-register

import datetime
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import numpy as np
from argon2 import PasswordHasher

ph = PasswordHasher()

try:
    scope = [
        'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name('ucpc-team-list-9acf2432120a.json', scope)

    _name = "UCPC Team List"
    client = gspread.authorize(creds)
    spreadsheet = client.open(_name)
    wks = spreadsheet.worksheet("List_teams")
    wks.update_cell(1,1, "Updating data using gspread")
except:
    pass

# Create your views here.
def home(request):
    context = {}
    return render(request, 'register/home.html', context)




class register(View):
    def get(self, request): 
        
        now = datetime.datetime.now()
        deadline = datetime.datetime(2023, 5, 25, 0, 0, 0, 0)
        time_remaining = deadline.day - now.day
        
        type = request.GET.get('type')
        if time_remaining > 0:
            context = {
                'tf': TeamForm, 
                'tmf': HighSchoolFormSet if type == 'HighSchool' else UniversityFormSet ,
                'isTimeOver': False
            }
        else:
            context = {
                'tf': TeamForm, 
                'tmf': HighSchoolFormSet if type == 'HighSchool' else UniversityFormSet,
                'isTimeOver': True
            }
        return render(request, 'register/register.html', context)
    
    def post(self, request):
        type = request.POST.get('type')
        if request.method == 'POST':
            tf = TeamForm(request.POST)
            tmf = HighSchoolFormSet(request.POST) if type == 'HighSchool' else UniversityFormSet(request.POST)
            if(tf.is_valid() and tmf.is_valid()):
                tf_data = tf.cleaned_data
                sheet_data = [tf_data.get('TeamName'), tf_data.get('Email')]
                try:
                    new_team_object = Team(TeamName = tf_data.get('TeamName'), Email = tf_data.get('Email'))
                    new_team_object.save()
                    
                    for index, tm in enumerate(tmf):
                        tmf_data = tm.cleaned_data 
                        new_teammate_object = Teammate(
                            Team = new_team_object, 
                            Fullname = tmf_data.get('Fullname'),
                            MSSV_CMND = tmf_data.get('MSSV_CMND'),
                            Phone = tmf_data.get('Phone'),
                            School = tmf_data.get('School'),
                            Leader = True if index == 0 else False,
                            Occupation = Choices.OCCUPATION_CHOICES[2][0] if index == 3 else Choices.OCCUPATION_CHOICES[1][0] if type == 'HighSchool' else Choices.OCCUPATION_CHOICES[0][0]
                        )
                        new_teammate_object.save()
                        
                        # sheet_data.append(
                        #     new_teammate_object.Fullname, 
                        #     new_teammate_object.MSSV_CMND, 
                        #     new_teammate_object.Phone, 
                        #     new_teammate_object.School, 
                        #     new_teammate_object.Leader, 
                        #     new_teammate_object.Occupation
                        # )

                    user = User.objects.create_user(username=tf_data.get('TeamName'), email=tf_data.get('Email'), password=tf_data.get('Password'))
                    user.save()

                    # idx = f'B{str(len(wks.get_all_values()) + 1)}'
                    # wks.update(idx, sheet_data.tolist())
                except Exception as ex:
                    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                    message = template.format(type(ex).__name__, ex.args)
                    print(message)
                    
                messages.success(request, '✔️ Tài khoản ' + tf_data.get('TeamName') + ' đã đăng ký thành công!')
                return redirect('register:login')
            else:
                ctx = {
                    'tf':tf,
                    'tmf': tmf
                }
                messages.error(request, '❌ Thông tin không hợp lệ!')
                return render(request, 'register/register.html', ctx, status=422)

class login(View):
    def get(self, request):
        ctx = {'lf': LoginForm}
        return render(request, 'login/login.html', ctx)
    def post(self, request):
        if request.method == 'POST':
            Username = request.POST['email']
            Password = request.POST['password']

            user = authenticate(request, username=Username, password=Password)

            if user is not None:
                auth_login(request, user)
                return redirect('register:profile')
            else:
                messages.error(request, '🙁 Email hoặc mật khẩu chưa chính xác!')
                return redirect('register:login')

@login_required         
def profile(request):
    data = Team.objects.filter(email=request.user.username)
    args = {'data':data, 'user':request.user}
    return render(request, 'login/profile.html', args)

# class edit(View):
#     def get(self, request):
#         emp = Team.objects.get(email=request.user.username)
#         ef = editForm(initial={'member1':emp.member1, 'cmnd1': emp.cmnd1, 'phone1': emp.phone1, 'member2':emp.member2, 'cmnd2': emp.cmnd2, 'phone2': emp.phone2,'member3':emp.member3, 'cmnd3': emp.cmnd3, 'phone3': emp.phone3,'school':emp.school})
#         return render(request, 'login/edit.html', {'ef':ef})
#     def post(self, request):
#         if request.method == 'POST':
#             ef = editForm(request.POST)
#             if ef.is_valid():
#                 emp = Team.objects.get(email=request.user.username)
#                 emp.member1 = ef.cleaned_data.get('member1')
#                 emp.member2 = ef.cleaned_data.get('member2')
#                 emp.member3 = ef.cleaned_data.get('member3')
#                 emp.cmnd1 = ef.cleaned_data.get('cmnd1')
#                 emp.cmnd2 = ef.cleaned_data.get('cmnd2')
#                 emp.cmnd3 = ef.cleaned_data.get('cmnd3')
#                 emp.phone1 = ef.cleaned_data.get('phone1')
#                 emp.phone2 = ef.cleaned_data.get('phone2')
#                 emp.phone3 = ef.cleaned_data.get('phone3')
#                 emp.school = ef.cleaned_data.get('school')
#                 emp.save()
#                 messages.success(request, '✔️ Update success! ')
#                 return redirect('register:profile')
#             else:
#                 ctx = {"ef":ef}
#                 messages.error(request, '❌ You entered an invalid value!')
#                 return render(request, 'login/edit.html', ctx)
            

def logout(request):
    auth_logout(request)
    return redirect('register:home')

