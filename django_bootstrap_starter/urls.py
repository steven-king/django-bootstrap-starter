from django.conf.urls import patterns, include, url
from django.views.generic.base import View
from testapp import views
from django.views import generic

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', generic.RedirectView.as_view(url='persons'), name='home' ),
    url(r'^person/add$', views.PersonCreate.as_view(), name='person_add'),
    url(r'^persons$', views.PersonList.as_view(), name='person_list'),
    
)