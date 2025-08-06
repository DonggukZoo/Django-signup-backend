from django.http import HttpResponse

def hello(request):
    return HttpResponse("안녕, 수현!")


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')