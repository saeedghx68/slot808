"""slot URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from myapp.views import *
from django.contrib.auth import views as djangoViews
from django.contrib import admin
from adminplus.sites import AdminSitePlus

admin.site = AdminSitePlus()
admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profile/$', profile, name='profile'),
    url(r'^get-lattery/$', get_lattery, name='get-lattery'),
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^changePass/$', change_password, name='change_password'),
    url(r'^password-reset/$', djangoViews.password_reset, name='password_reset'),
    url(r'^password-reset/done/$', djangoViews.password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        djangoViews.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', djangoViews.password_reset_complete, name='password_reset_complete'),
]
