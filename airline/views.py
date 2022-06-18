from email import header
from wsgiref import headers
from django.shortcuts import render
import requests
import json

# Create your views here.

def index(request):
    if 'airline' in request.GET:
        airline = request.GET['airline']
        url = 'https://api.api-ninjas.com/v1/airlines?name={}'.format(airline)
        response = requests.get(url, headers={'X-Api-Key': 'Uz6hdCAa/XFsk+YUx/zPoA==TRKc1smpxSZLrNHx'}).json()
        
        data = response[0]
        
        return render(request, 'index.html', {'data':data})
    return render(request, 'index.html')

def tracking(request):
    if 'airline' in request.GET:
        airline = request.GET['airline']
        url = 'https://api.api-ninjas.com/v1/airlines?name={}'.format(airline)
        response = request.get(url, headers={'X-Api-Key': 'Uz6hdCAa/XFsk+YUx/zPoA==TRKc1smpxSZLrNHx'})
        
        if response:
            print('successful')
        else:
            print('failed')
        
        return render(request, 'index.html', {'data':data})