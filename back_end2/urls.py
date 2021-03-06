"""back_end2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

from members.social_auth.views import FacebookLogin,TwitterLogin,FacebookConnect, TwitterConnect
from rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('members.api.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/twitter/$', TwitterLogin.as_view(), name='twitter_login'),
    path('rest-auth/facebook/connect/$', FacebookConnect.as_view(), name='fb_connect'),
    path('rest-auth/twitter/connect/$', TwitterConnect.as_view(), name='twitter_connect'),
    path('socialaccounts/$', SocialAccountListView.as_view(), name='social_account_list'),
    path('socialaccounts/(?P<pk>\d+)/disconnect/$', SocialAccountDisconnectView.as_view(),
        name='social_account_disconnect')

]
