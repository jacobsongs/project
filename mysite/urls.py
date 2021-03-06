from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^music/', include('music.urls', namespace="music")),
    url(r'^aboutus$', TemplateView.as_view(template_name="aboutus.txt", content_type="text/plain")),
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file")

]
