from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")

def pg1(request):
    return render(request,"pagina1.html")

def pg2(request):
    return render(request,"pagina2.html")

def pg3(request):
    return render(request,"pagina3.html")
    