from django.shortcuts import render, get_object_or_404
from .models import Pagina
from .forms import FormularioCadastro


# Create your views here.
def index(request):
    paginas = Pagina.objects.all()
    return render(request, 'geral/blog.html',
                  {'paginas': paginas})


def exibir(request, id_blog):
    blog = get_object_or_404(Pagina, id=id_blog)
    return render(request, 'geral/artigo.html',
                  {'blog': blog})


def cadastro(request):
    if request.method == 'GET':
        form = FormularioCadastro()
        return render(request, 'geral/nova_pagina.html', {'form': form})
    else:
        form = FormularioCadastro(request.POST)
        if form.is_valid():
            cadastro = form.save()
            form = FormularioCadastro()
            return index(request)
        else:
            return render(request, 'geral/form.html', {'form': form})