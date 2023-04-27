from django.shortcuts import render, redirect
from .forms import userForm, LoginForm, HighSchoolFormSet, UniversityFormSet, TeamForm
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from register.models import Team, Teammate, Post, Website, UcpcUser
from django.contrib.auth.decorators import login_required
from .choices import Choices

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
        deadline = datetime.datetime(2023, 5, 25)
        time_remaining = deadline - now
        if time_remaining.days < 0:
            context = {'uf': userForm, 'isTimeOver': True}
        else:
            context = {'uf': userForm, 'isTimeOver': False}

        return render(request, 'register/register.html', context)
    
    def post(self, request):
        if request.method == 'POST':
            uf = userForm(request.POST)
            if uf.is_valid():
                uf.save()

                data = np.array([[request.POST['email'], ph.hash(request.POST['password1'])]])
            
                idx = f'B{str(len(wks.get_all_values()) + 1)}' 
                wks.update(idx, data.tolist())
            
                email = uf.cleaned_data.get('email')
                messages.success(request, '✔️ Tài khoản ' + email + ' đã đăng ký thành công!')
                return redirect('register:login')
            else:
                ctx = {"uf":uf}
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
                return redirect('register:home')
            else:
                messages.error(request, '🙁 Email hoặc mật khẩu chưa chính xác!')
                return redirect('register:login')

# View classes handle functions related to user profiles 
class view_profile(View):
    # Display user profile
    def get(self, request):
        try:
            ucpc_user = UcpcUser.objects.get(email=request.user.email)
            filtered_team = Team.objects.get(UcpcUser=ucpc_user)
            filtered_teammates = Teammate.objects.filter(Team=filtered_team)
            ctx = {
                'user_email': request.user.email,
                'team': {
                    'TeamName': filtered_team.TeamName,
                    'FeePayment': filtered_team.FeePayment,
                    'Rank': filtered_team.Rank
                }, 
                'teammates': [
                    {
                        'Fullname': teammate.Fullname,
                        'MSSV_CMND': teammate.MSSV_CMND,
                        'Phone': teammate.Phone,
                        'School': teammate.School,
                        'Leader': teammate.Leader,
                        'Occupation': teammate.Occupation
                    } for teammate in filtered_teammates
                ]
            }
            return render(request, 'login/profile.html', ctx)   
        except:
            messages.error(request, '❌ Không tìm thấy đội thi. Vui lòng tạo đội thi mới!')
            return redirect('register:create')
        
class create_profile(View):
    # Display form to create user profile
    def get(self, request): 
        now = datetime.datetime.now()
        deadline = datetime.datetime(2023, 5, 25)
        time_remaining = deadline - now
        
        type = request.GET.get('type')
        if time_remaining.days > 0:
            ctx = {
                'tf': TeamForm, 
                'tmf': HighSchoolFormSet if type == 'HighSchool' else UniversityFormSet,
                'isTimeOver': False
            }
        else:
            ctx = {
                'tf': TeamForm, 
                'tmf': HighSchoolFormSet if type == 'HighSchool' else UniversityFormSet,
                'isTimeOver': True
            }
        return render(request, 'login/create.html', ctx)

    # Create new profile
    def post(self, request):
        if request.method == 'POST':
            type = request.POST.get('type')
            
            tf = TeamForm(request.POST)
            tmf = HighSchoolFormSet(request.POST) if type == 'HighSchool' else UniversityFormSet(request.POST)
        
            if(tf.is_valid() and tmf.is_valid()):
                tf_data = tf.cleaned_data
                try:
                    ucpc_user = UcpcUser.objects.get(email=request.user.email)
                    new_team = Team(
                        UcpcUser = ucpc_user,
                        TeamName = tf_data.get('TeamName')
                    )
                    new_team.save()
                    
                    for index, tm in enumerate(tmf):
                        tmf_data = tm.cleaned_data 
                        new_teammate = Teammate(
                            Team = new_team, 
                            Fullname = tmf_data.get('Fullname'),
                            MSSV_CMND = tmf_data.get('MSSV_CMND'),
                            Phone = tmf_data.get('Phone'),
                            School = tmf_data.get('School'),
                            Leader = True if index == 0 else False,
                            Occupation = Choices.OCCUPATION_CHOICES[2][0] if index == 3 else Choices.OCCUPATION_CHOICES[1][0] if type == 'HighSchool' else Choices.OCCUPATION_CHOICES[0][0]
                        )
                        new_teammate.save()
                        
                    messages.success(request, '✔️ Tài khoản ' + request.user.email + ' tạo đội thi thành công!')
                    return redirect('register:profile')
                except Exception as ex:
                    print(ex)
                    ctx = {
                        'tf':tf,
                        'tmf': tmf
                    }
                    messages.error(request, '❌ Lỗi hệ thống!')
                    return render(request, 'login/create.html', ctx, status=500)
            else:
                ctx = {
                    'tf':tf,
                    'tmf': tmf
                }
                messages.error(request, '❌ Thông tin không hợp lệ!')
                return render(request, 'login/create.html', ctx, status=422)
            
class edit_profile(View):
    def get(self, request): 
        now = datetime.datetime.now()
        deadline = datetime.datetime(2023, 5, 25)
        time_remaining = deadline - now
        
        type = request.GET.get('type')
        if time_remaining.days > 0:
            ucpc_user = UcpcUser.objects.get(email = request.user.email)
            filtered_team = Team.objects.get(UcpcUser = ucpc_user)
            filtered_teammates = Teammate.objects.filter(Team = filtered_team)

            tf_initial =  { 'TeamName': filtered_team.TeamName }
            tmf_initial = [
                {
                    'Fullname': teammate.Fullname,
                    'MSSV_CMND': teammate.MSSV_CMND,
                    'Phone': teammate.Phone,
                    'School': teammate.School      
                } for teammate in filtered_teammates
            ]
            
            ctx = {
                'tf': TeamForm(initial = tf_initial), 
                'tmf': HighSchoolFormSet(initial = tmf_initial) if type == 'HighSchool' else UniversityFormSet(initial = tmf_initial) ,
                'isTimeOver': False
            }
        else:
            ctx = {
                'tf': TeamForm, 
                'tmf': HighSchoolFormSet if type == 'HighSchool' else UniversityFormSet,
                'isTimeOver': True
            }
        return render(request, 'login/edit.html', ctx)
    
    def post(self, request):
        if request.method == 'POST':
            try:
                type = request.POST.get('type')
                ucpc_user = UcpcUser.objects.get(email = request.user.email)
                team_instance = Team.objects.get(UcpcUser = ucpc_user)
                tf = TeamForm(request.POST, instance=team_instance)
                if(tf.is_valid()):
                    team_instance = tf.save()
                teammates_instance = Teammate.objects.filter(Team = team_instance)
                tmf = HighSchoolFormSet(request.POST) if type == 'HighSchool' else UniversityFormSet(request.POST)
                for tm, teammate_instance in zip(tmf, teammates_instance):
                    tm.instance = teammate_instance
                if(tmf.is_valid()):
                    tmf.save()
                messages.success(request, '✔️ Tài khoản ' + request.user.email + ' cập nhật thông tin thành công!')
                return redirect('register:profile')
            except Exception as ex:
                print(ex)
                messages.error(request, '❌ Lỗi hệ thống!')
                return render(request, 'login/edit.html', status=500)
            # if (tf.is_valid() and tmf.is_valid()): 
            #     tf_instance = tf.save()
            #     for tm in tmf:
            #         tm.Team = tf_instance
            #         tm.save()
            #     messages.success(request, '✔️ Tài khoản ' + request.user.email + ' cập nhật thông tin thành công!')
            #     return redirect('register:profile')
            # else:
            #     ctx = { 
            #         'tf':tf,
            #         'tmf': tmf
            #     }
            #     messages.error(request, '❌ Thông tin không hợp lệ!')
            #     return render(request, 'login/edit.html', ctx, status=422)

def logout(request):
    auth_logout(request)
    return redirect('register:home')

