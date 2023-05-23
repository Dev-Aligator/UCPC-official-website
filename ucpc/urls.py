"""ucpc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from allauth.socialaccount import providers
from importlib import import_module
from django.contrib.auth import views as auth_views 
from register import views
from django.shortcuts import redirect
admin.site.site_title = "UCPC Administration"
admin.site.site_header = "Administration"
admin.site.index_title = "UCPC "

urlpatterns = [
    path('', lambda request: redirect('info/')),
    path('info/admin/', admin.site.urls),
    path('info/',include('register.urls')),
    path('info/',include('posting.urls')),
    # path('accounts/', include('allauth.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
]

if settings.SOCIALACCOUNT_ENABLED:
    urlpatterns += [path("social/", include("allauth.socialaccount.urls"))]


provider_urlpatterns = []
for provider in providers.registry.get_list():
    try:
        prov_mod = import_module(provider.get_package() + ".urls")
    except ImportError:
        continue
    prov_urlpatterns = getattr(prov_mod, "urlpatterns", None)
    if prov_urlpatterns:
        prov_urlpatterns = [path("info/" + str(url.pattern), include((url.url_patterns, url.namespace))) for url in prov_urlpatterns]
        provider_urlpatterns += prov_urlpatterns
urlpatterns += provider_urlpatterns