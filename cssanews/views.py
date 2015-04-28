from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
import json

@csrf_exempt  
def index(request):
	print "cssanews/index"
	context = {}
	return render(request, 'news/index.html', context)
# Create your views here.

@csrf_exempt  
def test(request):
	p = Article(title='Title', )
	response = {}
	context = {}
	print "@@"
	response['html'] = render_to_string("news/article.html", context)
	print "##"
	return JsonResponse(response)