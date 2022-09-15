from django import forms
from .models import *


class FormularioCadastro(forms.ModelForm):
    class Meta:
        model = Pagina
        fields = [
            'data',
            'conteudo',
            'categorias',
            'descricao',
            'titulo',
            'imagem',
            'autor',
        ]
