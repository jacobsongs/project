from django.conf.urls import include, url
from django.http import HttpResponse
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^music/', include('music.urls', namespace="music")),
    url(r'^robots.txt/', lambda x: HttpResponse("User-Agent: *\nDisallow:", content_type="text/plain"), name="robots_file")

]
