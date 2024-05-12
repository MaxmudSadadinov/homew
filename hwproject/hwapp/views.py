#from django.shortcuts import render
from django.http import HttpResponse
import logging



logger = logging.getLogger(__name__)


def about_me(request):
    
    with open('/home/max/Desktop/djj/hwproject/hwapp/about_me.html', 'r') as about:
        
        content = about.read()
        resp = HttpResponse(content)
        logger.debug(f'посетили страницу "about me"')
        return resp
    

def main(request):
    
    with open('/home/max/Desktop/djj/hwproject/hwapp/main.html', 'r') as main:
        content = main.read()
        resp = HttpResponse(content)
        logger.debug(f'посетили страницу "main"')
        return resp

