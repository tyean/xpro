"""xpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.views.generic import TemplateView
from django.contrib import admin
from xpro.views import custom_login, index_view, change_email, change_display_name

urlpatterns = [
    url(r'^$', index_view, name='home'),
    url(r'^aboutus/', TemplateView.as_view(template_name='AboutUs.html'), name='aboutus'),
    url(r'^admin/', admin.site.urls),
    url(r'^MyCalendar/', include('MyCalendar.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),

    # To stop logged in users from accessing login page
    url(r'^accounts/login/$', custom_login, name='login'),

    url(r'^accounts/', include('registration.backends.hmac.urls')),

    url(r'^change_email', change_email, name='changeemail'),
    url(r'^change_display_name', change_display_name, name='changedisplayname'),

]
