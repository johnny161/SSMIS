"""SSMIS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from control import views as control_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', control_views.signup, name="signup"), #登录
    url(r'^register/$', control_views.register, name="register"),#注册
    url(r'^logout/$', control_views.logout, name="logout"),  #登出
    url(r'^homepage/$', control_views.homepage, name="homepage"), #主页
    url(r'^selfinfohome/$', control_views.selfinfohome, name="selfinfohome"),  # 个人中心主页:显示个人信息
    url(r'^changepwd/$', login_required(control_views.changepwd), name="changepwd"),

    url(r'^createsociety/$',control_views.create_society,name="createsociety"),#创建社团
    url(r'^customizesociety/$', control_views.customize_society, name="customizesociety"),  # 定制社团数据对象
    url(r'^dataobject/(?P<object>[0-9]+)$', control_views.data_object, name='data_object'), #定制数据对象的字段
    url(r'^dataobject/(?P<object>[0-9]+)/addfield/$', control_views.add_field, name='add_field'),  # 增加数据对象的字段
    url(r'^edit/(?P<object_id>[0-9]+)$', control_views.edit_data_object, name="edit_data_object"),  # 修改社团数据对象
    url(r'^edit/action/$', control_views.edit_action, name='edit_action'),

    url(r'^managesociety/$', control_views.manage_society, name="managesociety"),  # 管理社团数据对象
    url(r'^managedataobject/(?P<object>[0-9]+)$', control_views.manage_data, name='manage_data'),  # 管理数据对象的数据
    url(r'^dataobject/(?P<object>[0-9]+)/adddata/$', control_views.add_data, name='add_data'),  # 增加数据对象的数据
]
