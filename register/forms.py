from django import forms
from django.forms import inlineformset_factory
from .models import Team, Teammate
from .validator import Validator
from .choices import Choices
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class userForm(UserCreationForm):
    email = forms.EmailField(label= 'Email', widget = forms.TextInput(attrs={'class': 'form-element form-box-control','placeholder': '✉️ |  Email Address' }))
    password1 = forms.CharField(max_length = 20, label = 'Mật khẩu', validators=[Validator.PwdRegex], widget = forms.PasswordInput(attrs={'class': 'form-element', 'id': 'pos5', 'placeholder': '🔒 | Password'}))
    password2 = forms.CharField(max_length = 20, label = 'Xác nhận mật khẩu', widget = forms.PasswordInput(attrs={'class': 'form-element', 'id': 'pos6', 'placeholder': '🔒 | Re-enter password'}))
    class Meta:
        model = get_user_model()
        fields = ['email']


class TeamForm(forms.ModelForm):
    TeamName = forms.CharField(required=True, max_length = 30, label = 'Tên đội', validators=[Validator.TeamRegex], widget = forms.TextInput(attrs={'class': 'form-box-control', 'id': 'pos1', 'placeholder': 'Chữ cái đầu tiên trong tên đội phải viết hoa. Ví dụ: Team01' }))
    class Meta:
        model = Team
        fields = ['TeamName']

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs) 

        # add custom error messages
        self.fields['TeamName'].error_messages.update({
            'invalid': '⚠️ Tên đội không hợp lệ! (Tên đội hợp lệ có độ dài tối đa 30 ký tự với duy nhất chữ cái in hoa ở đầu)',
        })

class TeammateForm(forms.ModelForm):
    Fullname = forms.CharField(required=True, max_length=30, label='Họ và tên', validators=[Validator.NameRegex], widget = forms.TextInput(attrs={'class': 'form-box-control', 'placeholder': 'Ví dụ: Nguyễn Văn A', 'name': 'Fullname' }))
    MSSV_CMND = forms.CharField(required=True, max_length=12, label = 'MSSV/CMND', validators=[Validator.MSSV_CMNDRegex], widget = forms.TextInput(attrs={'class': 'form-box-control', 'placeholder': 'MSSV có 8 chữ số hoặc CMND/CCCD có 9/12 chữ số. Ví dụ: 381932123'}))
    Phone = forms.CharField(required=True, max_length=11, label = 'Số điện thoại', validators=[Validator.PhoneRegex], widget = forms.TextInput(attrs={'class': 'form-box-control', 'id': 'pos2', 'placeholder': 'Số điện thoại có 10 hoặc 11 chữ số. Ví dụ: 0912345678'}))
    School = forms.ChoiceField(required=True, label='Tên trường', choices=Choices.SCHOOL_CHOICES, widget=forms.Select(attrs={'class': 'form-box-control', 'list': 'schools', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))
    
    def __init__(self, *args, **kwargs):
        super(TeammateForm, self).__init__(*args, **kwargs)
        self.fields['Fullname'].error_messages.update({
            'invalid': '⚠️ Tên không hợp lệ!',
        })
        self.fields['MSSV_CMND'].error_messages.update({
            'invalid': '⚠️ Mã số sinh viên / Chứng minh nhân dân không hợp lệ! (MSSV hợp lệ có 8 chữ số / CMND hợp lệ có 9 hoặc 12 chữ số)',
        })
        self.fields['Phone'].error_messages.update({
            'invalid': '⚠️ Số điện thoại không hợp lệ! (Số điện thoại hợp lệ có 10 hoặc 11 chữ số)',
        }) 
        
    class Meta:
        model = Teammate
        fields = ['Fullname', 'MSSV_CMND', 'Phone', 'School']
    
HighSchoolFormSet = inlineformset_factory(
    parent_model=Team, 
    model=Teammate, 
    form=TeammateForm,
    extra=4
)

UniversityFormSet = inlineformset_factory (
    parent_model=Team,
    model=Teammate,
    form=TeammateForm,
    extra=3
)



class LoginForm(forms.Form):
    Email = forms.EmailField(required=True, label= 'Email', widget = forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Ví dụ: abcd@efgh.com' }))
    Password = forms.CharField(required=True, max_length = 20, label = 'Mật khẩu', validators=[Validator.PwdRegex], widget = forms.PasswordInput(attrs={'class': 'form-control'}))
