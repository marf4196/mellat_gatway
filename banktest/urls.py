"""banktest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from payments import views
from azbankgateways.urls import az_bank_gateways_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^request/$', views.send_request, name='request'),
    url(r'^verify/$', views.verify , name='verify'),
    path('bankgateways/', az_bank_gateways_urls()),
    path('go-to-gateway/', views.go_to_gateway_view),
    path('callback-gateway/', views.callback_gateway_view),
]
