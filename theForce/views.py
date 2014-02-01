# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
#core
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from forms import MyRegistrationForm
from django.contrib.auth.decorators import login_required
#models
from simple_salesforce import Salesforce
import json
def index(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect("/loggedin")
	else:
		c = {}
		c.update(csrf(request))
		sf = Salesforce(username='whatsupsj@gmail.com', password='Junkmail1!', security_token='GxJyxvdyKRkWqIySzha8w7xT')
		contact = sf.query("SELECT Id, CloseDate, CreatedDate, Amount FROM Opportunity")
		records = contact["records"]
		i,a,t,close = [],[],[],[]
		for item in records:
			i.append(item["Id"])
			a.append(item["Amount"])
			close.append(item["CloseDate"])
			t.append(item["CreatedDate"])		
		
		lst = [{'ID': d[0], 'Amount': d[1], 'CloseDate': d[2], 'CreatedDate': d[3]} for d in zip(i, a, close, t)]
		c['contact'] = lst
		return render_to_response('index.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	currentPath = request.POST.get('currentPath', '')
	currentPath = currentPath.replace("invalid/", "").replace("registered/", "")
	if user is not None:
		auth.login(request, user)
		if "log" in currentPath:
			return HttpResponseRedirect(currentPath)
		else:
			return HttpResponseRedirect('/loggedin')
	else:
		if "log" in currentPath:
			return HttpResponseRedirect(currentPath + "invalid")
		else:
			return HttpResponseRedirect('/invalid')

@login_required(login_url="/")
def loggedin(request):
	return render_to_response('loggedin.html', {'user': request.user,})

def invalid_login(request):
	c = {}
	c.update(csrf(request))
	form = MyRegistrationForm()
	form.fields['password1'].label = "密码"
	form.fields['password2'].label = "再次输入密码"
	c["form"] = form
	c['last_invalid'] = True
	return render_to_response('index.html', c)

def logout(request):
	auth.logout(request)
	c = {}
	c.update(csrf(request))
	form = MyRegistrationForm()
	form.fields['password1'].label = "密码"
	form.fields['password2'].label = "再次输入密码"
	c["form"] = form
	return render_to_response('index.html', c)

def register_user(request):
	currentPath = request.POST.get('currentPath', '')
	currentPath = currentPath.replace("invalid/", "").replace("registered/", "")
	username=request.POST.get('email')
	password=request.POST.get('password1')
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			user = auth.authenticate(username=username, password=password)

			if user is not None:
				auth.login(request, user)
			if "log" in currentPath:
				return HttpResponseRedirect(currentPath)
			else:
				return HttpResponseRedirect('/register_success')
		elif "log" in currentPath:
			return HttpResponseRedirect(currentPath + "registered")
	else:
		form = MyRegistrationForm()
		form.fields['password1'].label = "密码"
		form.fields['password2'].label = "再次输入密码"
	args = {}
	args.update(csrf(request))
	
	args['form'] = form
	
	return render_to_response('register.html', args)


def register_success(request):
	return HttpResponseRedirect('/loggedin')