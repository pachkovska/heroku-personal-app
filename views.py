import requests
import glob
import os
from django.http import HttpResponse
from django.shortcuts import render

content_files = glob.glob('templates/content/*.html')

pages = []

for content_file in  content_files:
    file_name = os.path.basename(content_file)
    name_only, extention = os.path.splitext(file_name)
    pages.append({
        "content_file_name": content_file, 
        "title": name_only if file_name != 'index.html' else 'home',
    })

def index(request):
    content_html = open('templates/content/index.html').read()
    context = {
    "index": content_html,
    }
    return render(request, "base.html", context)



