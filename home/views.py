from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
   response = HttpResponse()
   response.writelines('<h1>Xin chào</h1>')
   response.write('Đây là app home')
   return response

def helo(request):
   response = HttpResponse()
   response.writelines('<h1>o</h1>')
   response.write('home')
   return response
def dieu(request):
   response = HttpResponse()
   response.writelines('dieu')
   response.write('aa')
   return response