"""dweb URL Configuration

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
from drug.views import *
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'build_socket/(?P<user_id>[0-9]+)$', build_socket, name='build_socket'),
    url(r'send_socket/$', send_socket, name='send_socket'),
    url(r'index/$', TemplateView.as_view(template_name='drugcon.html'), name='index'),
    url(r'index2/$', TemplateView.as_view(template_name='drugcon2.html'), name='index2'),
]
