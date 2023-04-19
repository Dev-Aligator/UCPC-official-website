from django.shortcuts import render, redirect
from .forms import TeamForm, LoginForm, TeammateFormSet
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .models import Team, Teammate, Website
from django.contrib.auth.decorators import login_required

import datetime
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import numpy as np
from argon2 import PasswordHasher

ph = PasswordHasher()

try:
    scope =[
        'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"]
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
        if time_remaining > 0:
            context = {
                'tf': TeamForm, 
                'tmf': TeammateFormSet,
                'isTimeOver': False
            }
        else:
            context = {
                'tf': TeamForm, 
                'tmf': TeammateFormSet,
                'isTimeOver': True
            }
        return render(request, 'register/register.html', context)
    
    def post(self, request):
        if request.method == 'POST':
            tf = TeamForm(request.POST)
            tmf = TeammateFormSet(request.POST)
            if all(tf.is_valid(), tmf.is_valid()):
                tf.save()

                # Username = request.POST['TeamName']
                # Email = request.POST['Email']
                # Password = request.POST['Password']
                # user = User.objects.create_user(Username, Email, Password)
                # user.save()

                # data = np.array([[request.POST['Team'],
                #                   request.POST['Email'],
                #                   ph.hash(request.POST['Password']), 
                #                   request.POST['Teammate1'],
                #                   request.POST['Age1'],
                #                   request.POST['CMND1'],
                #                   request.POST['Phone1'],
                #                   request.POST['Occupation1'],
                #                   request.POST['School1'],
                #                   request.POST['MSSV1'],
                #                   request.POST['Teammate2'],
                #                   request.POST['Age2'],
                #                   request.POST['CMND2'],
                #                   request.POST['Phone2'],
                #                   request.POST['Occupation2'],
                #                   request.POST['School2'],
                #                   request.POST['MSSV2'],
                #                   request.POST['Teammate3'],
                #                   request.POST['Age3'],
                #                   request.POST['CMND3'],
                #                   request.POST['Phone3'],
                #                   request.POST['Occupation3'],
                #                   request.POST['School3'],
                #                   request.POST['MSSV3'],
                #                   request.POST['Teacher'],
                #                   request.POST['CMNDTC'],
                #                   request.POST['PhoneTC'],
                #                   request.POST['OccupationTC'],
                #                   request.POST['SchoolTC'],
                #                 ]])
                # try:
                #     idx = f'B{str(len(wks.get_all_values()) + 1)}'
                #     wks.update(idx, data.tolist())
                # except:
                #     pass

                Team = tf.cleaned_data.get('TeamName')
                messages.success(request, '✔️ Tài khoản '+Team+' đã đăng ký thành công!')
                return redirect('register:login')
            else:
                ctx = {"tf":tf}
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
    


# class TeamRegister(CreateView):
#     model = Team
#     fields = ['TeamName', 'Email']
    
#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         if self.request.POST:
#             data['Teammate1'] = UserFormSet(self.request.POST)
#             data['Teammate2'] = UserFormSet(self.request.POST)
#             data['Teammate3'] = UserFormSet(self.request.POST)
#             data['Teacher'] = UserFormSet(self.request.POST)
#         else:
#             data['Teammate1'] = UserFormSet()
#             data['Teammate2'] = UserFormSet()
#             data['Teammate3'] = UserFormSet()
#             data['Teacher'] = UserFormSet()
            
#         now = datetime.datetime.now()
#         deadline = Website.Deadline
#         time_remaining = deadline - now
#         data['Overtime'] = True if time_remaining > 0 else False
        
#         return data
    
#     def form_valid(self, form):
#         context = self.get_context_data()
#         children_context = {
#             'teammate1': context['Teammate1'], 
#             'teammate2': context['Teammate2'],
#             'teammate3': context['Teammate3'],
#             'teacher': context['Teacher']
#         }
#         self.object = form.save()
#         if(all(child_context.is_valid() for child_context in children_context.values())):
#             for child_context in children_context.values():
#                 child_context.instance = self.object
#                 child_context.save()
#         return super().form_valid(form)
        
