from django.shortcuts import render, get_object_or_404
from .models import Pagina


# Create your views here.
def index(request):
    paginas = Pagina.objects.all()
    return render(request, 'geral/blog.html', {'paginas': paginas})
