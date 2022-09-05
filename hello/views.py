from django.shortcuts import render
from django.http import HttpResponse
import requests

# import graphgeneration
from .analysisCompletedata import CompleteAnalysis
from .graphgeneration import Graphgen
from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

# def index(request):
#     r = requests.get('https://httpbin.org/status/418')
#     print(r.text)
#     return HttpResponse('<pre>' + r.text + '</pre>')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def graph(request):

    graphgen=Graphgen()
    completeana=CompleteAnalysis()
    graphgen.__init__()
    completeana.__init__()
    graphgens=Graphgen.genrateGraph("")
    completeanalysis=CompleteAnalysis.getCompleteAnalysis("")
    # return HttpResponse(Graphgen.genrateGraph(''))
    # exec(open("/Users/payel/Python/A-study-on-autism/hello/"+"graphgeneration.py").read())
    return render(request,"graph.html",completeanalysis)