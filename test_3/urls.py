"""test_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from stockanalysis import views
urlpatterns = [
    url(r'^admin/', admin.site.urls,name='admin'),
    url(r'^recommand/', views.recommand, name='profile'),
    #url(r'^profile/', views.form2, name='profile'),
    url(r'^signup/', views.form1, name='signup'),
    url(r'^login/',views.login,name='login'),
    url(r'^home/',views.index2,name='home'),
    url(r'^', views.index),
    #url(r'^profile/(?P<item_id>[0-9]+)/$', views.profile, name='user profile')
    #url(r'^',views.home),
]
