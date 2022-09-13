from django.shortcuts import render, get_object_or_404
from .models import Pagina


# Create your views here.
def index(request):
    paginas = Pagina.objects.all()
    return render(request, 'geral/blog.html',
                  {'paginas': paginas})


def exibir(request, id_blog):
    blog = get_object_or_404(Pagina, id=id_blog)
    return render(request, 'geral/exibir_paginas.html',
                  {'blog': blog})