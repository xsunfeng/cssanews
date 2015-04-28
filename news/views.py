from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from news.models import Article
import json
import pytz
import datetime

import urllib2
from bs4 import BeautifulSoup

def index(request):
	print "index"
	context = {}
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
	title = request.REQUEST.get('title','').encode('utf-8')
	author = request.REQUEST.get('author', '').encode('utf-8')
	content = request.REQUEST.get('content', '').encode('utf-8')
	tz = pytz.timezone("US/Eastern")
	print title, author, content
	print tz.localize(datetime.datetime.now())
	tmp = Article(title=title, author=author, content=content, pub_date=tz.localize(datetime.datetime.now()))
	tmp.save()
	response = {}
	return HttpResponse(json.dumps(response), content_type='application/json')

@csrf_exempt  
def detail(request, news_id):
	print "detail"
	article = Article.objects.get(id = news_id)
	try:
		print news_id
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'news/article.html', {'article': article})

@csrf_exempt  
def delete(request):
	print "delete"
	article_id = request.REQUEST.get('article_id','')
	print type(article_id)
	a = Article.objects.get(id=int(str(article_id)))
	try:
		a.delete()
	except:
    		print "Unexpected error:", sys.exc_info()[0]
	return render(request, 'news/article.html', {})

@csrf_exempt  
def extract_url(request):
	response = {}
 	action = request.REQUEST.get('action')
	url = request.REQUEST.get('url')
	if True: #action == 'add-doc-from-url':
		try:
			header = {
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
				'Accept-Encoding':'deflate, sdch',
				'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
				'Cache-Control':'no-cache',
				'Connection':'keep-alive',
				'Host':'www.centredaily.com',
				'Pragma':'no-cache',
				'Cache-Control': 'no-cache',
				'Referer':'http://www.centredaily.com/',
				'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
			}

			req = urllib2.Request(
                    			url = url,
                    			# headers = header
                		)

			print url
			resp = urllib2.urlopen(req)
			print "2"
			html_page = resp.read()
			print "3"
			soup = BeautifulSoup(html_page)
			# date = soup.find('span', {'class' :'grd'}).text
			# moddate = soup.find('span', {'class' :'moddate'}).text
			print "4"
			title = soup.find('h2', {'class' :'rich_media_title'}).encode('utf-8')
			content = soup.find("div", class_="rich_media_content").encode('utf-8')
			print "###############"
			response["title"] = title
			response["content"] = content
			print response["title"]
			print response["content"]
			print "@@@@@@@@@@@@"
			print "5"
			print type(title)
			print type(content)
			tmp = json.dumps({"title": title, "content": content})
			print "6"
			return HttpResponse(tmp, content_type="application/json")
		except urllib2.HTTPError, e:
			print 'error', e.code
	else:
		print "else"
		req = urllib2.Request(url)
		resp = urllib2.urlopen(req)
		the_page = resp.read()
		response["title"] = ""
		response["content"] = the_page
	print response["title"] 
	print response["content"] 
    	return HttpResponse(json.dumps(response), content_type='application/json')
