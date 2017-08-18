from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def register(request):
    full_path =  request.get_full_path()
    
    if "register" in full_path or "new" in full_path:
        response = "placeholder for users to create a new user record"
    elif "login" in full_path:
        response = "placeholder for users to login"
    elif "users" in full_path:
        response = "placeholder to later display all the list of users"
    return HttpResponse(response)
