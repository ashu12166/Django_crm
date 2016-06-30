from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext

def User(request):
	title='title'
	return render(request, 'crm/userlogin.html', {})

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('crm/userlogin.html', {'c' : c}, context_instance=RequestContext(request) )


def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	import pdb
	pdb.set_trace()
	user = auth.authenticate(username=username , password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/acounts/invalid')

def loggedin(request):
	return render_to_response('post_list.html',
								{'username': request.user.first_name})