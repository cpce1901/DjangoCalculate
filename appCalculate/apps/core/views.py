from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def inicio(request):
    template = loader.get_template("core/index.html")
    context = {
        "titulo" : "Inicio"
    }
    return HttpResponse(template.render(context, request))

