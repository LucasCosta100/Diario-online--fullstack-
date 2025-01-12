from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")

def escrever(request):
    if request.method == "GET":
        return render(request, "escrever.html")
    elif request.method == "POST":
        titulo = request.POST.get("titulo") #"get" é usado quando se tem so um tipo de informação
        tags = request.POST.getlist("tags") #"getlist" é usado quando se tem multiplos tipos de informações
        pessoas = request.POST.getlist("pessoas")
        texto = request.POST.get("texto")
        return HttpResponse(f"{titulo} - {tags} - {pessoas} - {texto}")