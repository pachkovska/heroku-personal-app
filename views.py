import requests
import glob
import os
import re
from django.http import HttpResponse
from django.shortcuts import render


content_files = sorted(glob.glob('./templates/content/*.html'))

print(content_files)
print(type(content_files))

pages = []

for content_file in  content_files:
    file_name = os.path.basename(content_file)
    name_only, extention = os.path.splitext(file_name)
    cleansed_name = re.sub(r'\d_', '', name_only)
    pages.append({
        "page_name": cleansed_name if file_name != '1_index.html' else "home",
    })

def index(request): 
    context = {
    "pages": pages,
    "active_link": "home"
    }
    return render(request, "content/1_index.html", context)

def projects(request):
    context = {
    "pages": pages,
    "active_link": "projects"
    }
    return render(request, "content/2_projects.html", context)

def resume(request):
    # response = requests.get('https://api.github.com/users/pachkovska/repos')
    response = requests.get('https://api.github.com/users/pachkovska/repos/:pachkovska/:heroku-personal-app/stats/commit_activity')
    repos = response.json()
    context = {
    "pages": pages,
    "active_link": "resume",
    "repos": repos
    }
    return render(request, "content/3_resume.html", context)

def blog(request):
    context = {
    "pages": pages,
    "active_link": "blog"
    }
    return render(request, "content/4_blog.html", context)

def contact(request):
    context = {
    "pages": pages,
    "active_link": "contact"
    }
    return render(request, "content/5_contact.html", context)