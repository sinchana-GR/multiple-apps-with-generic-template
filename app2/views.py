from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_string(request):
    return HttpResponse('app1_string response')
def app2_htmlpage(request):
    return render(request,'app2_htmlpage.html')
    