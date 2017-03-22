from django.conf.urls import include, url
from django.http import HttpResponse
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^music/', include('music.urls', namespace="music")),
    (r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")),
]
