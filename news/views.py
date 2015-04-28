from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from news.models import Article
import json
import pytz
import datetime

def index(request):
	print "index"
	return render(request, 'news/index.html', context)
# Create your views here.

@csrf_exempt  
def edit(request):
	print "edit"
	context = {}
	return render(request, 'news/edit.html', context)

@csrf_exempt  
def list(request):
	print "list"
	context = {'articles': Article.objects.all(),}
	return render(request, 'news/article-list.html', context)

@csrf_exempt  
def add(request):
	print "add"
	title = request.REQUEST.get('title','')
	author = request.REQUEST.get('author', '')
	content = request.REQUEST.get('content', '')
	print "1"
	tz = pytz.timezone("US/Eastern")
	print title, author, content
	print tz.localize(datetime.datetime.now())
	tmp = Article(title=title, author=author, content=content, pub_date=tz.localize(datetime.datetime.now()))
	print "2"
	tmp.save()
	print "3"
	response = {}
	return HttpResponse(json.dumps(response), mimetype='application/json')

def detail(request, news_id):
    	try:
        		print news_id
    	except Question.DoesNotExist:
        		raise Http404("Question does not exist")
    	return render(request, 'news/article.html', {'news_id': news_id})