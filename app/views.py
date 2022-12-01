from django.shortcuts import render

# Create your views here.
def hai(request):
    return render(request,'hai.html')

def hello(request):
    return render(request,'hello.html')