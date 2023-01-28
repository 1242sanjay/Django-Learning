"""wscubetech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wscubetech import views

# for media work
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin-pannel/', admin.site.urls),
    path('', views.homePage, name='home'),
    path('courses/', views.courses, name='courses'),
    path('courses/<slug:courseid>', views.courseDetails),
    path('about-us/', views.aboutUs, name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('events/', views.events, name='events'),
    path('trainer/', views.trainer, name='trainer'),
    path('user-form/', views.userForm, name='userform'),
    path('submitform/', views.submitForm, name='submitform'),
    path('calculator/', views.calculator),
    path('newsdetails/<news_slug>', views.newsDetails),
    path('savecontact/', views.contactMessage, name='savecontact')
]


if settings.DEBUG:
    urlPatterns=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

