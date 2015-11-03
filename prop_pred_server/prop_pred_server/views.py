from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
	template = loader.get_template('index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def login(request):
	template = loader.get_template('login.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def maps(request):
	template = loader.get_template('gmaps.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))