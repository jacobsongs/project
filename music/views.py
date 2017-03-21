from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album
from django.http import HttpResponse
import logging

logger = logging.getLogger('ex_logger')
logger.info("core.views logger")  # should work                                                                                                         

def url_please(request):
    logger.info("path: %s" % request.path)  # should work                                                                                               
    return HttpResponse(request.path)

class IndexView(generic.ListView):
	template_name="Music/index.html"
	context_object_name='all_albums'
	
	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model=Album
	template_name='Music/detail.html'

class AlbumCreate(CreateView):
	model=Album
	fields=['artist','album_title','genre','album_logo']

