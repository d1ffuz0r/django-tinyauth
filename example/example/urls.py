from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()


class HomeView(TemplateView):
    template_name = 'home.html'


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view()),
    url('', include('django_tinyauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
