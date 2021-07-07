from django.http import HttpResponse


def hello(request):
	return HttpResponse("<i><h1>hello world</h1></i>")
