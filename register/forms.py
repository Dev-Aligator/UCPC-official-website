from distutils.command.clean import clean
from django import forms
from .models import Team
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
PasswordRegex = RegexValidator(r'^(?=.{6,})(?=.*[a-z]+)(?=.*\d+)(?=.*[A-Z]+)[ -~]*$')


class userForm(UserCreationForm):
    email = forms.EmailField(label= 'Email', widget = forms.TextInput(attrs={'class': 'form-element','placeholder': '✉️ |  Email Address' }))
    password1 = forms.CharField(max_length = 20, label = 'Mật khẩu', validators=[PasswordRegex], widget = forms.PasswordInput(attrs={'class': 'form-element', 'id': 'pos5', 'placeholder': '🔒 | Password'}))
    password2 = forms.CharField(max_length = 20, label = 'Xác nhận mật khẩu', widget = forms.PasswordInput(attrs={'class': 'form-element', 'id': 'pos6', 'placeholder': '🔒 | Re-enter password'}))
    class Meta:
        model = get_user_model()
        fields = ['email']

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError("This email address is already taken.")
    #     return email
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.username = self.clean_email()
    #     if commit:
    #         user.save()
    #     return user


class teamForm(forms.ModelForm):
    team = forms.CharField(max_length = 30, label = 'Tên đội',widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos1', 'placeholder': 'Chữ cái đầu tiên trong tên đội phải viết hoa. Ví dụ: Team01' }))
    
    member1 = forms.CharField(max_length = 30, label = 'Tên đội trưởng', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Nguyễn Văn A' }))
    mssv1 = forms.CharField(max_length=30, label = 'Mã số sinh viên', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mã số sinh viên bao gồm chữ số hoặc chữ thường và chữ số. Ví dụ: 21520001'}))
    cmnd1 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CMND/CCCD có 9 hoặc 12 chữ số. Ví dụ: 381932123'}))
    phone1 = forms.CharField(max_length=11, label = 'Số điện thoại', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos2', 'placeholder': 'Số điện thoại có 10 hoặc 11 chữ số. Ví dụ: 0912345678'}))
    school1 = forms.CharField(max_length=100, label='Trường', widget=forms.TextInput(attrs={'class': 'form-control', 'list': 'schools', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))

    member2 = forms.CharField(max_length = 30, label = 'Tên thành viên 2', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Nguyễn Văn B' }))
    mssv2 = forms.CharField(max_length=30, label = 'Mã số sinh viên', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mã số sinh viên bao gồm chữ số hoặc chữ thường và chữ số. Ví dụ: 21520001'}))
    cmnd2 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CMND/CCCD có 9 hoặc 12 chữ số. Ví dụ: 381932123'}))
    phone2 = forms.CharField(max_length=11, label = 'Số điện thoại', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos3', 'placeholder': 'Số điện thoại có 10 hoặc 11 chữ số. Ví dụ: 0912345678'}))
    school2 = forms.CharField(max_length=100, label='Trường', widget=forms.TextInput(attrs={'class': 'form-control', 'list': 'schools', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))

    member3 = forms.CharField(max_length = 30, label = 'Tên thành viên 3', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Nguyễn Văn C' }))
    mssv3 = forms.CharField(max_length=30, label = 'Mã số sinh viên', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mã số sinh viên bao gồm chữ số hoặc chữ thường và chữ số. Ví dụ: 21520001'}))
    cmnd3 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CMND/CCCD có 9 hoặc 12 chữ số. Ví dụ: 381932123'}))
    phone3 = forms.CharField(max_length=11, label = 'Số điện thoại', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos4', 'placeholder': 'Số điện thoại có 10 hoặc 11 chữ số. Ví dụ: 0912345678'}))
    school3 = forms.CharField(max_length=100, label='Trường', widget=forms.TextInput(attrs={'class': 'form-control', 'list': 'schools', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))

    email = forms.CharField(label= 'Email', widget = forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ví dụ: abcd@efgh.com' }))
    class Meta:
        model = Team
        fields = ['team', 'member1', 'mssv1', 'cmnd1', 'phone1', 'school1', 'member2', 'mssv2', 'cmnd2', 'phone2', 'school2', 'member3', 'mssv3', 'cmnd3', 'phone3', 'school3', 'email']
    password = forms.CharField(max_length = 20, label = 'Mật khẩu', validators=[PasswordRegex], widget = forms.PasswordInput(attrs={'class': 'form-control', 'id': 'pos5', 'placeholder': 'Mật khẩu phải có ít nhất 6 chữ số, bao gồm chữ thường, chữ in hoa và chữ số'}))
    rpassword = forms.CharField(max_length = 20, label = 'Xác nhận mật khẩu', widget = forms.PasswordInput(attrs={'class': 'form-control', 'id': 'pos6', 'placeholder': 'Nhập lại mật khẩu'}))

    def __init__(self, *args, **kwargs):
        super(teamForm, self).__init__(*args, **kwargs)

        # self.fields['school1'].label = "Trường"
        # self.fields['school2'].label = "Trường"
        # self.fields['school3'].label = "Trường"

        # add custom error messages
        self.fields['team'].error_messages.update({
            'invalid': '⚠️ Tên đội không hợp lệ!',
        })
        self.fields['member1'].error_messages.update({
            'invalid': '⚠️ Tên thành viên không hợp lệ!',
        })
        self.fields['mssv1'].error_messages.update({
            'invalid': '⚠️ Mã số sinh viên không hợp lệ! (Mã số sinh viên hợp lệ bao gồm chữ số hoặc chữ thường và chữ số)',
        })
        self.fields['cmnd1'].error_messages.update({
            'invalid': '⚠️ Số CMND/CCCD không hợp lệ! (CMND/CCCD hợp lệ có 9 hoặc 12 chữ số)',
        })
        self.fields['phone1'].error_messages.update({
            'invalid': '⚠️ Số điện thoại không hợp lệ! (Số điện thoại hợp lệ có 10 hoặc 11 chữ số)',
        })
        self.fields['member2'].error_messages.update({
            'invalid': '⚠️ Tên thành viên không hợp lệ!',
        })
        self.fields['mssv2'].error_messages.update({
            'invalid': '⚠️ Mã số sinh viên không hợp lệ! (Mã số sinh viên hợp lệ phải là chữ số)',
        })
        self.fields['cmnd2'].error_messages.update({
            'invalid': '⚠️ Số CMND/CCCD không hợp lệ! (CMND/CCCD hợp lệ có 9 hoặc 12 chữ số)',
        })
        self.fields['phone2'].error_messages.update({
            'invalid': '⚠️ Số điện thoại không hợp lệ! (Số điện thoại hợp lệ có 10 hoặc 11 chữ số)',
        })
        self.fields['member3'].error_messages.update({
            'invalid': '⚠️ Tên thành viên không hợp lệ!',
        })
        self.fields['mssv3'].error_messages.update({
            'invalid': '⚠️ Mã số sinh viên không hợp lệ! (Mã số sinh viên hợp lệ phải là chữ số)',
        })
        self.fields['cmnd3'].error_messages.update({
            'invalid': '⚠️ Số CMND/CCCD không hợp lệ! (CMND/CCCD hợp lệ có 9 hoặc 12 chữ số)',
        })
        self.fields['phone3'].error_messages.update({
            'invalid': '⚠️ Số điện thoại không hợp lệ! (Số điện thoại hợp lệ có 10 hoặc 11 chữ số)',
        })
        self.fields['email'].error_messages.update({
            'invalid': '⚠️ Địa chỉ email không hợp lệ!',
        })
        self.fields['password'].error_messages.update({
            'invalid': '⚠️ Mật khẩu không hợp lệ! (Mật khẩu hợp lệ có ít nhất 6 chữ số, bao gồm chữ thường, chữ in hoa và chữ số)',
        })

    def clean(self):
        cleaned_data = super(teamForm, self).clean()
        valpwd = cleaned_data.get('password')
        valrpwd = cleaned_data.get('rpassword')
        
        if valpwd and valrpwd:
            if valpwd != valrpwd:
                error_msg = '⚠️ Mật khẩu không khớp!'
                self.add_error('rpassword', error_msg)


class loginForm(forms.Form):
    email = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length = 20, label = 'Mật khẩu', widget = forms.PasswordInput(attrs={'class': 'form-control'}))

class editForm(forms.ModelForm):
    member1 = forms.CharField(max_length = 30, label = 'Name of member 1', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn A' }))
    mssv1 = forms.CharField(max_length=30, label = 'Mã số sinh viên', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mã số sinh viên bao gồm chữ số hoặc chữ thường và chữ số. Ví dụ: 21520001'}))
    cmnd1 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: 381932123'}))
    phone1 = forms.CharField(max_length=11, label = 'Phone', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos2', 'placeholder': 'example: 0912345678'}))
    school1 = forms.CharField(max_length=100, label='Trường', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))

    member2 = forms.CharField(max_length = 30, label = 'Name of member 2', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn B' }))
    mssv2 = forms.CharField(max_length=30, label = 'Mã số sinh viên', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mã số sinh viên bao gồm chữ số hoặc chữ thường và chữ số. Ví dụ: 21520001'}))
    cmnd2 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: 381932123'}))
    phone2 = forms.CharField(max_length=11, label = 'Phone', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos3', 'placeholder': 'example: 0912345678'}))
    school2 = forms.CharField(max_length=100, label='Trường', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))

    member3 = forms.CharField(max_length = 30, label = 'Name of member 3', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn C' }))
    mssv3 = forms.CharField(max_length=30, label = 'Mã số sinh viên', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mã số sinh viên bao gồm chữ số hoặc chữ thường và chữ số. Ví dụ: 21520001'}))
    cmnd3 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: 381932123'}))
    phone3 = forms.CharField(max_length=11, label = 'Phone', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos4', 'placeholder': 'example: 0912345678'}))
    school3 = forms.CharField(max_length=100, label='Trường', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))
    class Meta:
        model = Team
        fields = ['team', 'member1', 'mssv1', 'cmnd1', 'phone1', 'school1', 'member2', 'mssv2', 'cmnd2', 'phone2', 'school2', 'member3', 'mssv3', 'cmnd3', 'phone3', 'school3', 'email']
    