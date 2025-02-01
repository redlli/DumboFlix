from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.

class homeView(ListView):
	model=Post
	template_name='template/home.html'
	#return render(request,"home.html",{})
	
def movies(request):
	return render(request,"template/movies.html",{})
	
def about(request):
	return render(request,"template/about.html",{})
	

def loginview(request):
	
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		#aunticating
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request, user)
			messages.success(request,"got in baby!")
			return redirect("home")
		else:
			messages.success(request,"got not in baby!")
			return redirect('login')
	else:
		return render(request,"template/login.html",{})
	

def logout_user(request):
	logout(request)
	messages.success(request,"Logout baby!")
	return redirect ('home')
class PostView(DetailView):
	model=Post
	template_name='template/post_view.html'

class add_post(CreateView):
	model = Post
	template_name='template/add_post.html'
	fields='__all__'
	
