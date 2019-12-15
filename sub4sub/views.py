from django.shortcuts import render, redirect

def returnToHome(request):
	return redirect('home:index')