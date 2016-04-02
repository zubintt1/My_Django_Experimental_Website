from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_site_lander(request):
	text = "<h1>Hello Lander.You are welcome here</h1>"
	return HttpResponse(text)

def hello_world(request):
	# text = "<h1>Hello World!!</h1>"
	# return HttpResponse(text)
	return render(request, "My_Django_Experimental_Website_App/template/hello_world.html", {})