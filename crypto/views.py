from django.shortcuts import render

def home(request):
  import requests
  import json
  api_request = requests.get("https://jsonplaceholder.typicode.com/posts/1")
  api = json.loads(api_request.content)
  return render(request, 'home.html',{'api':api})
