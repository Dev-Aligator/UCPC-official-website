from distutils.command.clean import clean
from django import forms
from django.forms import inlineformset_factory
from .models import Team, User, Post
from validator import Validator
from choices import Choices

# class teamForm(forms.ModelForm):
#     team = forms.CharField(max_length = 30, label = 'Tên đội',widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos1', 'placeholder': 'Chữ cái đầu tiên trong tên đội phải viết hoa. Ví dụ: Team01' }))
    
#     member1 = forms.CharField(max_length = 30, label = 'Tên đội trưởng', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Nguyễn Văn A' }))
#     mssv1 = forms.CharField(max_length=30, label = 'Mã số sinh viên', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mã số sinh viên bao gồm chữ số hoặc chữ thường và chữ số. Ví dụ: 21520001'}))
#     cmnd1 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CMND/CCCD có 9 hoặc 12 chữ số. Ví dụ: 381932123'}))
#     phone1 = forms.CharField(max_length=11, label = 'Số điện thoại', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos2', 'placeholder': 'Số điện thoại có 10 hoặc 11 chữ số. Ví dụ: 0912345678'}))
#     school1 = forms.CharField(max_length=100, label='Trường', widget=forms.TextInput(attrs={'class': 'form-control', 'list': 'schools', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))

#     member2 = forms.CharField(max_length = 30, label = 'Tên thành viên 2', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Nguyễn Văn B' }))
#     mssv2 = forms.CharField(max_length=30, label = 'Mã số sinh viên', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mã số sinh viên bao gồm chữ số hoặc chữ thường và chữ số. Ví dụ: 21520001'}))
#     cmnd2 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CMND/CCCD có 9 hoặc 12 chữ số. Ví dụ: 381932123'}))
#     phone2 = forms.CharField(max_length=11, label = 'Số điện thoại', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos3', 'placeholder': 'Số điện thoại có 10 hoặc 11 chữ số. Ví dụ: 0912345678'}))
#     school2 = forms.CharField(max_length=100, label='Trường', widget=forms.TextInput(attrs={'class': 'form-control', 'list': 'schools', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))

#     member3 = forms.CharField(max_length = 30, label = 'Tên thành viên 3', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Nguyễn Văn C' }))
#     mssv3 = forms.CharField(max_length=30, label = 'Mã số sinh viên', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mã số sinh viên bao gồm chữ số hoặc chữ thường và chữ số. Ví dụ: 21520001'}))
#     cmnd3 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CMND/CCCD có 9 hoặc 12 chữ số. Ví dụ: 381932123'}))
#     phone3 = forms.CharField(max_length=11, label = 'Số điện thoại', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos4', 'placeholder': 'Số điện thoại có 10 hoặc 11 chữ số. Ví dụ: 0912345678'}))
#     school3 = forms.CharField(max_length=100, label='Trường', widget=forms.TextInput(attrs={'class': 'form-control', 'list': 'schools', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))

#     email = forms.CharField(label= 'Email', widget = forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ví dụ: abcd@efgh.com' }))
#     class Meta:
#         model = Team
#         fields = ['team', 'member1', 'mssv1', 'cmnd1', 'phone1', 'school1', 'member2', 'mssv2', 'cmnd2', 'phone2', 'school2', 'member3', 'mssv3', 'cmnd3', 'phone3', 'school3', 'email']
#     password = forms.CharField(max_length = 20, label = 'Mật khẩu', validators=[PasswordRegex], widget = forms.PasswordInput(attrs={'class': 'form-control', 'id': 'pos5', 'placeholder': 'Mật khẩu phải có ít nhất 6 chữ số, bao gồm chữ thường, chữ in hoa và chữ số'}))
#     rpassword = forms.CharField(max_length = 20, label = 'Xác nhận mật khẩu', widget = forms.PasswordInput(attrs={'class': 'form-control', 'id': 'pos6', 'placeholder': 'Nhập lại mật khẩu'}))

#     def __init__(self, *args, **kwargs):
#         super(teamForm, self).__init__(*args, **kwargs)

#         # self.fields['school1'].label = "Trường"
#         # self.fields['school2'].label = "Trường"
#         # self.fields['school3'].label = "Trường"

#         # add custom error messages
#         self.fields['team'].error_messages.update({
#             'invalid': '⚠️ Tên đội không hợp lệ!',
#         })
#         self.fields['member1'].error_messages.update({
#             'invalid': '⚠️ Tên thành viên không hợp lệ!',
#         })
#         self.fields['mssv1'].error_messages.update({
#             'invalid': '⚠️ Mã số sinh viên không hợp lệ! (Mã số sinh viên hợp lệ bao gồm chữ số hoặc chữ thường và chữ số)',
#         })
#         self.fields['cmnd1'].error_messages.update({
#             'invalid': '⚠️ Số CMND/CCCD không hợp lệ! (CMND/CCCD hợp lệ có 9 hoặc 12 chữ số)',
#         })
#         self.fields['phone1'].error_messages.update({
#             'invalid': '⚠️ Số điện thoại không hợp lệ! (Số điện thoại hợp lệ có 10 hoặc 11 chữ số)',
#         })
#         self.fields['member2'].error_messages.update({
#             'invalid': '⚠️ Tên thành viên không hợp lệ!',
#         })
#         self.fields['mssv2'].error_messages.update({
#             'invalid': '⚠️ Mã số sinh viên không hợp lệ! (Mã số sinh viên hợp lệ phải là chữ số)',
#         })
#         self.fields['cmnd2'].error_messages.update({
#             'invalid': '⚠️ Số CMND/CCCD không hợp lệ! (CMND/CCCD hợp lệ có 9 hoặc 12 chữ số)',
#         })
#         self.fields['phone2'].error_messages.update({
#             'invalid': '⚠️ Số điện thoại không hợp lệ! (Số điện thoại hợp lệ có 10 hoặc 11 chữ số)',
#         })
#         self.fields['member3'].error_messages.update({
#             'invalid': '⚠️ Tên thành viên không hợp lệ!',
#         })
#         self.fields['mssv3'].error_messages.update({
#             'invalid': '⚠️ Mã số sinh viên không hợp lệ! (Mã số sinh viên hợp lệ phải là chữ số)',
#         })
#         self.fields['cmnd3'].error_messages.update({
#             'invalid': '⚠️ Số CMND/CCCD không hợp lệ! (CMND/CCCD hợp lệ có 9 hoặc 12 chữ số)',
#         })
#         self.fields['phone3'].error_messages.update({
#             'invalid': '⚠️ Số điện thoại không hợp lệ! (Số điện thoại hợp lệ có 10 hoặc 11 chữ số)',
#         })
#         self.fields['email'].error_messages.update({
#             'invalid': '⚠️ Địa chỉ email không hợp lệ!',
#         })
#         self.fields['password'].error_messages.update({
#             'invalid': '⚠️ Mật khẩu không hợp lệ! (Mật khẩu hợp lệ có ít nhất 6 chữ số, bao gồm chữ thường, chữ in hoa và chữ số)',
#         })

#     def clean(self):
#         cleaned_data = super(teamForm, self).clean()
#         valpwd = cleaned_data.get('password')
#         valrpwd = cleaned_data.get('rpassword')
        
#         if valpwd and valrpwd:
#             if valpwd != valrpwd:
#                 error_msg = '⚠️ Mật khẩu không khớp!'
#                 self.add_error('rpassword', error_msg)

class TeamForm(forms.ModelForm):
    TeamName = forms.CharField(required=True, max_length = 30, label = 'Tên đội', validators=[Validator.TeamRegex], widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos1', 'placeholder': 'Chữ cái đầu tiên trong tên đội phải viết hoa. Ví dụ: Team01' }))
    Email = forms.EmailField(required=True, label= 'Email', widget = forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Ví dụ: abcd@efgh.com' }))
    
    class Meta:
        model = Team
        fields = ['TeamName', 'Email']

    Password = forms.CharField(required=True, max_length = 20, label = 'Mật khẩu', validators=[Validator.PwdRegex], widget = forms.PasswordInput(attrs={'class': 'form-control', 'id': 'pos5', 'placeholder': 'Mật khẩu phải có ít nhất 6 chữ số, bao gồm chữ thường, chữ in hoa và chữ số'}))
    RPassword = forms.CharField(required=True, max_length = 20, label = 'Xác nhận mật khẩu', validators=[Validator.PwdRegex], widget = forms.PasswordInput(attrs={'class': 'form-control', 'id': 'pos6', 'placeholder': 'Nhập lại mật khẩu'}))
    
    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs) 

        # add custom error messages
        self.fields['TeamName'].error_messages.update({
            'invalid': '⚠️ Tên đội không hợp lệ!',
        })
        self.fields['Email'].error_messages.update({
            'invalid': '⚠️ Địa chỉ email không hợp lệ!',
        })
        self.fields['Password'].error_messages.update({
            'invalid': '⚠️ Mật khẩu không hợp lệ! (Mật khẩu hợp lệ có ít nhất 6 chữ số, bao gồm chữ thường, chữ in hoa và chữ số)',
        })
        self.fields['RPassword'].error_messages.update({
            'invalid': '⚠️ Mật khẩu không hợp lệ! (Mật khẩu hợp lệ có ít nhất 6 chữ số, bao gồm chữ thường, chữ in hoa và chữ số)',
        })

    def clean(self):
        cleaned_data = super(TeamForm, self).clean()
        valpwd = cleaned_data.get('Password')
        valrpwd = cleaned_data.get('RPassword')
        
        if valpwd and valrpwd:
            if valpwd != valrpwd:
                error_msg = '⚠️ Mật khẩu không khớp!'
                self.add_error('RPassword', error_msg)

class UserForm(forms.ModelForm):
    Fullname = forms.CharField(required=True, max_length=30, label='Tên đội trưởng', validators=[Validator.NameRegex], widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Nguyễn Văn A' }))
    MSSV_CMND = forms.CharField(required=True, max_length=12, label = 'CMND/CCCD', validators=[Validator.MSSV_CMNDRegex], widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CMND/CCCD có 9 hoặc 12 chữ số. Ví dụ: 381932123'}))
    Phone = forms.CharField(required=True, max_length=11, label = 'Số điện thoại', validators=[Validator.PhoneRegex], widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos2', 'placeholder': 'Số điện thoại có 10 hoặc 11 chữ số. Ví dụ: 0912345678'}))
    School = forms.ChoiceField(required=True, label='Trường', choices=Choices.SCHOOL_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'list': 'schools', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['Teammate1'].error_messages.update({
            'invalid': '⚠️ Tên thành viên không hợp lệ!',
        })
        self.fields['MSSV_CMND'].error_messages.update({
            'invalid': '⚠️ Mã số sinh viên / Chứng minh nhân dân không hợp lệ! (MSSV hợp lệ có 8 chữ số / CMND hợp lệ có 9 hoặc 12 chữ số)',
        })
        self.fields['Phone'].error_messages.update({
            'invalid': '⚠️ Số điện thoại không hợp lệ! (Số điện thoại hợp lệ có 10 hoặc 11 chữ số)',
        }) 
        
    class Meta:
        model = User
        fields = ['Fullname', 'MSSV_CMND', 'Phone', 'School']
    
UserFormSet = inlineformset_factory(
    parent_model=Team, 
    model=User, 
    form=UserForm,
    extra=1,
    can_delete=True,
)



class LoginForm(forms.Form):
    Email = forms.EmailField(required=True, label= 'Email', widget = forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Ví dụ: abcd@efgh.com' }))
    Password = forms.CharField(required=True, max_length = 20, label = 'Mật khẩu', validators=[Validator.PwdRegex], widget = forms.PasswordInput(attrs={'class': 'form-control'}))

class EditForm(forms.ModelForm):
    Teammate1 = forms.CharField(required=True, max_length=30, label='Tên đội trưởng', validators=[Validator.NameRegex], widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Nguyễn Văn A' }))
    Age1 = forms.IntegerField(required=True, label='Tuổi', validators=[Validator.AgeRegex], widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Độ tuổi từ 16 đến 23 tuổi'}))
    CMND1 = forms.CharField(required=True, max_length=12, label = 'CMND/CCCD', validators=[Validator.CMNDandCCCD], widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CMND/CCCD có 9 hoặc 12 chữ số. Ví dụ: 381932123'}))
    Phone1 = forms.CharField(required=True, max_length=11, label = 'Số điện thoại', validators=[Validator.PhoneRegex], widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos2', 'placeholder': 'Số điện thoại có 10 hoặc 11 chữ số. Ví dụ: 0912345678'}))
    Occupation1 = forms.ChoiceField(required=True, label='Nghề nghiệp', widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Nghề nghiệp hiện tại'}))
    School1 = forms.ChoiceField(required=True, label='Trường', widget=forms.Select(attrs={'class': 'form-control', 'list': 'schools', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))
    MSSV1 = forms.CharField(required=True, max_length=30, label = 'Mã số sinh viên', validators=[Validator.MSSVRegex], widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mã số sinh viên bao gồm chữ số hoặc chữ thường và chữ số. Ví dụ: 21520001'}))

    Teammate2 = forms.CharField(required=True, max_length = 30, label = 'Tên thành viên 2', validators=[Validator.NameRegex], widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Nguyễn Văn B' }))
    Age2 = forms.IntegerField(required=True, label='Tuổi', validators=[Validator.AgeRegex], widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Độ tuổi từ 16 đến 23 tuổi'}))
    CMND2 = forms.CharField(required=True, max_length=12, label = 'CMND/CCCD', validators=[Validator.CMNDandCCCD], widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CMND/CCCD có 9 hoặc 12 chữ số. Ví dụ: 381932123'}))
    Phone2 = forms.CharField(required=True, max_length=11, label = 'Số điện thoại', validators=[Validator.PhoneRegex], widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos3', 'placeholder': 'Số điện thoại có 10 hoặc 11 chữ số. Ví dụ: 0912345678'}))
    Occupation2 = forms.ChoiceField(required=True, label='Nghề nghiệp', widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Nghề nghiệp hiện tại'}))
    School2 = forms.ChoiceField(required=True, label='Trường', widget=forms.Select(attrs={'class': 'form-control', 'list': 'schools', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))
    MSSV2 = forms.CharField(required=True, max_length=30, label = 'Mã số sinh viên', validators=[Validator.MSSVRegex], widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mã số sinh viên bao gồm chữ số hoặc chữ thường và chữ số. Ví dụ: 21520001'}))

    Teammate3 = forms.CharField(required=True, max_length = 30, label = 'Tên thành viên 3', validators=[Validator.NameRegex], widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Nguyễn Văn C' }))
    Age3 = forms.IntegerField(required=True, label='Tuổi', validators=[Validator.AgeRegex], widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Độ tuổi từ 16 đến 23 tuổi'}))
    CMND3 = forms.CharField(required=True, max_length=12, label = 'CMND/CCCD', validators=[Validator.CMNDandCCCD], widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CMND/CCCD có 9 hoặc 12 chữ số. Ví dụ: 381932123'}))
    Phone3 = forms.CharField(required=True, max_length=11, label = 'Số điện thoại', validators=[Validator.PhoneRegex], widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos4', 'placeholder': 'Số điện thoại có 10 hoặc 11 chữ số. Ví dụ: 0912345678'}))
    Occupation3 = forms.ChoiceField(required=True, label='Nghề nghiệp', widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Nghề nghiệp hiện tại'}))
    School3 = forms.ChoiceField(required=True, label='Trường', widget=forms.Select(attrs={'class': 'form-control', 'list': 'schools', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))
    MSSV3 = forms.CharField(required=True, max_length=30, label = 'Mã số sinh viên', validators=[Validator.MSSVRegex], widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mã số sinh viên bao gồm chữ số hoặc chữ thường và chữ số. Ví dụ: 21520001'}))

    Teacher = forms.CharField(required=True, max_length = 30, label = 'Tên thành viên 3', validators=[Validator.NameRegex], widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ví dụ: Nguyễn Văn C' }))
    CMNDTC = forms.CharField(required=True, max_length=12, label = 'CMND/CCCD', validators=[Validator.CMNDandCCCD], widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CMND/CCCD có 9 hoặc 12 chữ số. Ví dụ: 381932123'}))
    PhoneTC = forms.CharField(required=True, max_length=11, label = 'Số điện thoại', validators=[Validator.PhoneRegex], widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos4', 'placeholder': 'Số điện thoại có 10 hoặc 11 chữ số. Ví dụ: 0912345678'}))
    OccupationTC = forms.ChoiceField(required=True, label='Nghề nghiệp', widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Nghề nghiệp hiện tại'}))
    SchoolTC = forms.ChoiceField(required=True, label='Trường', widget=forms.Select(attrs={'class': 'form-control', 'list': 'schools', 'placeholder': 'Ví dụ: Đại học Công nghệ Thông tin - ĐHQG TP.HCM'}))
    
    class Meta:
        model = Team
        fields = ['TeamName', 'Email', 'Password', 'RPassword', 'Teammate1', 'Age1', 'CMND1', 'Phone1', 'Occupation1', 'School1', 'MSSV1', 'Teammate2', 'Age2', 'CMND2', 'Phone2', 'Occupation2', 'School2', 'MSSV2', 'Teammate3', 'Age3', 'CMND3', 'Phone3', 'Occupation3', 'School3', 'MSSV3', 'Teacher', 'CMNDTC', 'PhoneTC', 'OccupationTC', 'SchoolTC']
        