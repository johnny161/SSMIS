from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, Http404, HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from django.utils import timezone
from django.template import RequestContext
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from control.data_layer_connector.private_method import *
from control.data_layer_connector.base_method import *
from control.data_layer_connector.bussiness1 import *
from control.data_layer_connector.saas_method import *
from control.data_layer_connector.bussiness1 import *
import MySQLdb

def signup(request):
   # if request.user.is_authenticated:
    #    return redirect('homepage')
    if request.method == 'POST':
        lf = LoginForm(request.POST)
        if lf.is_valid():
            _Username = lf.cleaned_data['username']
            _Password = lf.cleaned_data['password']
            user = auth.authenticate(username=_Username, password=_Password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('homepage')
            else:
                return HttpResponse(u"用户或密码错误")
    else:
        lf = LoginForm()
    return render(request, 'signup.html', {'lf': lf, })

def register(request):
  #  if request.user.is_authenticated:
   #     return redirect('homepage')
    if request.method == 'POST':
        rf = RegistForm(request.POST)
        if rf.is_valid():
            _Username = request.POST.get('username')
            _Password = request.POST.get('password')
            _Password2 = request.POST.get('passwordagain')
            _Email = request.POST.get('email')
            _Grade_college_major = request.POST.get('grade_college_major')
            _Realname = request.POST.get('realname')

            if _Password != _Password2:
                return HttpResponse(u"两次密码不一致")
            filterResult = User.objects.filter(username=_Username)  # c************
            if len(filterResult) > 0:
                return HttpResponse("用户名已存在")

            user = User.objects._create_user(username=_Username, password=_Password, email=_Email,  )
            account = Account()
            account.user_id = user.id
            account.grade_college_major = _Grade_college_major
            account.realname = _Realname
            account.save()
            auth.login(request, user)
            return redirect('homepage')
    else:
        rf = RegistForm()
    return render(request, 'register.html', {'rf': rf, })

# 主页的部分
@login_required(login_url='/')
def homepage(request):
    user = request.user
    #membership = Account_Community.objects.filter(account=user)
    response = render_to_response('homepage.html', {'user': user, })
    response.set_cookie('username', user, 3600)
    return response

@login_required(login_url="/")
def logout(request):
    auth.logout(request)
    respon = HttpResponseRedirect('/')
    respon.delete_cookie('username')
    respon.delete_cookie('member')
    return respon

# 个人中心
@login_required(login_url="/")
def selfinfohome(request):
    user = request.user
    #membership = Account_Community.objects.filter(account=user)
    profile = user.account
    return render(request, 'selfinfo-home.html', {'user': user, 'profile': profile}) #, 'memberships': membership}

@login_required(login_url="/")
@csrf_protect
def changepwd(request):
    user = request.user
    if request.method == 'GET':
        form = ChangepwdForm()
        return render(request, 'changepwd.html', {'user': user,'form': form, })
    else:
        form = ChangepwdForm(request.POST)
        if form.is_valid():
            username = request.user.username
            oldpassword = request.POST.get('oldpassword', '')
            user = auth.authenticate(username=username, password=oldpassword)
            if user is not None and user.is_active:
                newpassword = request.POST.get('newpassword1', '')
                user.set_password(newpassword)
                user.save()
                lf = LoginForm()
                return render(request, 'signup.html', {'lf': lf,})
            else:
                return render(request, 'changepwd.html', {'user': user,'form': form, 'oldpassword_is_wrong': True})
        else:
            return render(request,'changepwd.html', {'user': user,'form': form, })

@login_required(login_url="/")
def create_society(request):
    if request.method == 'POST':
        csf = CreateSocietyForm(request.POST)
        if csf.is_valid():
            _tenantname = request.POST.get('tenantname')
            _tenantintroduction = request.POST.get('tenantintroduction')
            tenant = Tenant()
            tenant.tenantname=_tenantname
            tenant.tenantintroduction=_tenantintroduction
            tenant.user=request.user
            tenant.save()
            return redirect('selfinfohome')
    else:
        csf = CreateSocietyForm()
    return render(request, 'selfinfo-createsociety.html', {'csf': csf,'create_is_wrong': True})

def customize_society(request):
    user_id=request.user.id
    tenant_id = Tenant.objects.get(user_id=user_id).tenantid
    objects = get_table_list_new(tenant_id)
    return render(request, 'selfinfo-customorgan.html' ,{'objects':objects})

def data_object(request, object):
    user_id = request.user.id
    tenant_id = Tenant.objects.get(user_id=user_id).tenantid
    lists = get_field_list(object, tenant_id)
    return render(request, 'selfinfo-customorgan-data_object.html', {'object': object, 'lists': lists})

def edit_data_object(request,object_id):
    if str(object_id) == '0':
        return render(request, 'selfinfo-customorgan-edit_data_object.html')
    user_id=request.user.id
    tenant_id=Tenant.objects.get(user_id=user_id).tenantid
    objects=get_table_list(tenant_id)
    return render(request, 'selfinfo-customorgan-edit_data_object.html')

def edit_action(request):
    tableName = request.POST.get('tableName')
    object_id = request.POST.get('object_id', 0)
    user_id=request.user.id
    tenant_id = Tenant.objects.get(user_id=user_id).tenantid
    objects = get_table_list(tenant_id)
    for tenant in Tenant.objects.filter(user_id=user_id):
        tenant_id=tenant.tenantid

    if object_id == '0':
        create_table(tenant_id,tableName)
        return render(request, 'selfinfo-customorgan.html',{'objects':objects})

    create_table(tenant_id,tableName)
    return render(request, 'selfinfo-customorgan.html',{'objects':objects})

def add_field(request,object):
    if request.method == 'POST':
        aff = AddFieldForm(request.POST)
        if aff.is_valid():
            _name = aff.cleaned_data['column_name']
            _type = aff.cleaned_data['column_type']
            user_id = request.user.id
            tenant_id = Tenant.objects.get(user_id=user_id).tenantid
            add_field_new(tenant_id, int(object), _name, _type)
            lists = get_field_list(object, tenant_id)
            return render(request, 'selfinfo-customorgan-data_object.html', {'object': object,'lists':lists})
    else:
        aff = AddFieldForm()
    return render(request, 'selfinfo-customorgan-add.html', {'aff': aff})
