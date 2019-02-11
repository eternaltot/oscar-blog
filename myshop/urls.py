"""myshop URL Configuration

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
from django.conf.urls import include, url  # < Django-2.0
from django.contrib import admin
from oscar.app import application
from blogs.app import application as blogs_app
from dashboard.blogs.app import application as blogs_dashboard_app
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # path('admin/', admin.site.urls),  # > Django-2.0

    url(r'', application.urls),
    # path('', application.urls),  # > Django-2.0
    url(r'^dashboard/blog/', include(blogs_dashboard_app.urls)),
    url(r'^blog/', include(blogs_app.urls)),
]
