from django.shortcuts import render

# Create your views here.

def nout(request):
    return render(request, 'nout.html')

def about(request):
    return render(request, 'about.html')

