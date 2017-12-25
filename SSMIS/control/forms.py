from django import forms
from django.forms import ModelForm
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(label=u'学号', required=True, max_length=30)
    password = forms.CharField(label=u'密码', required=True, widget=forms.PasswordInput(), max_length=20)


class RegistForm(forms.Form):
    username = forms.CharField(label=u"账号", required=True, )
    password = forms.CharField(label=u"密码", required=True, widget=forms.PasswordInput())
    passwordagain = forms.CharField(label=u"确认密码", required=True, widget=forms.PasswordInput())
    grade_college_major = forms.CharField(label=u'年级学院专业', required=True)
    realname = forms.CharField(label=u'真实姓名', required=True)
    email = forms.EmailField(label=u'邮箱', required=True)


class ChangepwdForm(forms.Form):
    oldpassword = forms.CharField(
        required=True,
        label=u"原密码",
        error_messages={'required': u'请输入原密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u"原密码",
                'rows': 1,
            }
        ),
    )
    newpassword1 = forms.CharField(
        required=True,
        label=u"新密码",
        error_messages={'required': u'请输入新密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u"新密码",
                'rows': 1,
            }
        ),
    )
    newpassword2 = forms.CharField(
        required=True,
        label=u"确认密码",
        error_messages={'required': u'请再次输入新密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u"确认密码",
                'rows': 1,
            }
        ),
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"所有项都为必填项")
        elif self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
            raise forms.ValidationError(u"两次输入的新密码不一样")
        else:
            cleaned_data = super(ChangepwdForm, self).clean()
        return cleaned_data


class CreateSocietyForm(ModelForm):
    class Meta:
        model = Tenant
        fields = ['tenantname', 'tenantcategory','tenantbelong','tenantcampus','tenantintroduction']

class AddFieldForm(forms.Form):
    column_name=forms.CharField(label=u"字段名称",required=True)
    column_type=forms.CharField(label=u"字段类型",required=True)

class AddDataForm(forms.Form):
    v0 = forms.CharField(max_length=20,required=False)
    v1 = forms.CharField(max_length=20,required=False)
    v2 = forms.CharField(max_length=20,required=False)
    v3 = forms.CharField(max_length=20,required=False)
    v4 = forms.CharField(max_length=20,required=False)
    v5 = forms.CharField(max_length=20,required=False)
    v6 = forms.CharField(max_length=20,required=False)
    v7 = forms.CharField(max_length=20,required=False)
    v8 = forms.CharField(max_length=20,required=False)
    v9 = forms.CharField(max_length=20,required=False)