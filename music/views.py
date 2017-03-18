from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album

def get_ip_address(request):
    """ use requestobject to fetch client machine's IP Address """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')    ### Real IP address of client Machine
    return ip   


def home(request):
    """ your vies to handle http request """
    ip_address = get_ip_address(request)
    
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

