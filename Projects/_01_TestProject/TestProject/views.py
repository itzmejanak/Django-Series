from django.http import HttpResponse
from django.shortcuts import render
def TestRoute(req):
    return HttpResponse("Test Successfully excuted")
    
def DynamicRoute(req, data):
    return HttpResponse(f"Your data is: <h1 style='color:red'>{data}</h1>")
    
def RenderHtml(req):
   return render(req, 'index.html')
   
def DataHtml(req):
    data = {
    "data":["janak", "Devkota", "21 Years"],
    "title":"Data | Janak"
    }
    return render(req, 'dataHtml.html', data)

def StaticLearn(req):
    return render(req, 'static.html')


def home(req):
    return render(req, 'home.html')

def About(req):
    return render(req, 'about.html')

def Form(req):
    ans = 0
    try:
        n1 = int(req.GET.get("num1"))
        n2 = int(req.GET.get("num2"))
        ans = n1+n2
        print(ans)
    except:
        pass
    return render(req, 'form.html', {"ans":ans})