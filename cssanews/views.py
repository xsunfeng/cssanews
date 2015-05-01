from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
import json

@csrf_exempt  
def index(request):
	print "cssanews/index"
	context = {}
	if request.user.is_authenticated():
		print "there is a user"
		username = str(request.user)
		context['username'] = username
	else:
		print "there is no user"
	return render(request, 'news/index.html', context)

#account

from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response

@csrf_exempt  
def register_view(request):
    print "register_view"
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", {
        'form': form,
    })

@csrf_exempt  
def login_view(request):
	context = {}
	if request.method != 'POST':
		return render(request, 'registration/login.html', context)
	try:
		username = request.POST['username'];
		password = request.POST['password'];
		user = auth.authenticate(username = username, password = password)
		if user is not None:
			auth.login(request, user)
			return HttpResponse("You are logged in.")
		else:
			return HttpResponse("Invalid password.")
	except e:
		return HttpResponse("Your username and password didn't match.")

def logout_view(request):
	auth.logout(request)
	# Redirect to a success page.
	return HttpResponse("logged out")