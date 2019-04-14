"""website URL Configuration

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
from exchange.views import *




urlpatterns = [
	url(r'^admin/', admin.site.urls, name='home'),
	url(r'^demouser_1', hello, name='hello'),
	url(r'^a', test, name='test'),
	url(r'^', hello, name='hello'),
	url(r'^demouser_2', demouser_2, name='sell'),
	#url(r'^$', redirect('https://idprep.kuveytturk.com.tr/api/connect/authorize?client_id=7cd8964b46564b12a6bbec30d96bfcfc&scope=accounts%20offline_access&response_type=code&redirect_uri=https://www.ahmetsutbas.com.tr/callback&state=abc'))

]		