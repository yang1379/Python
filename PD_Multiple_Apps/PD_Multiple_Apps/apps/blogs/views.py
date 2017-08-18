'''
Multiple Apps
Objectives
Get familiar with setting up a new Django project
Get familiar with setting up a new Django app
Get familiar with routing
Get familiar with views and how to render simple Http Response
With Django, it's easy to create multiple apps that can be used across multiple projects.  Let's say that you're a freelancer and have worked with many clients in the past.  Say that the particular industry your clients are in, almost every single project you've worked on, every client/project wants their own blogs, surveys, and user management system.  Instead of having to re-create these modules each time from scratch, you decide to create three independent apps that you can use throughout all of these projects.

Using what you've learned, please do the following:

Create a new project 
Create three apps
Have the following URL either display a simple HttpResponse or redirect to a different URL for the following apps
blogs app
/blogs - display "placeholder to later display all the list of blogs" via HttpResponse. Have this be handled by a method named 'index'.
/blogs/new - display "placeholder to display a new form to create a new blog" via HttpResponse. Have this be handled by a method named 'new'.
/blogs/create - Have this be handled by a method named 'create'.  For now, have this url redirect to /blogs.
/blogs/{{number}} - display 'placeholder to display blog {{number}}.  For example /blogs/15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'.
/blogs/{{number}}/edit - display 'placeholder to edit blog {{number}}.  Have this be handled by a method named 'edit'.
/blogs/{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /blogs. 
surveys app
/surveys - display "placeholder to display all the surveys created"
/surveys/new - display "placeholder for users to add a new survey
users app
/register - display 'placeholder for users to create a new user record'
/login - display 'placeholder for users to login' 
/users/new - have the same method that handles /register also handle the url request of /users/new
/users - display 'placeholder to later display all the list of users'
Have the root route (e.g. localhost/) be handled by the index method in the blogs' view file.
'''
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, blog_num):
    response = "placeholder to display blog {}".format(blog_num)
    return HttpResponse(response)

def edit(request, blog_num):
    response = "placeholder to edit blog {}".format(blog_num)
    return HttpResponse(response)

def destroy(request, blog_num):
    return redirect('/')

