from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
import pyshorteners
# Create your views here.
from . import service

def shorten(request, url):
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.chilpit.short(url)
    return HttpResponse(f'Shortened URL: <a href="{shortened_url}">{shortened_url}</a>')


def index(request):
    return render(request, 'main/index.html')


def shorten_post(request):
    return shorten(request, request.POST['url'])


def redirect_hash(request, url_hash):
    original_url = service.load_url(url_hash).original_url
    return redirect(original_url)


from . import service


def shorten(request, url):
    shortened_url_hash = service.shorten(url)
    shortened_url = request.build_absolute_uri(reverse('redirect', args=[shortened_url_hash]))
    return render(request, 'main/link.html', {'shortened_url': shortened_url})