from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm

# View para listar os livros
def lista_livros(request):
    livros = Livro.objects.all() # busca no banco
    return render(
        request, 'acervo/lista.html',
        {'livros': livros} # envia ao template
    )

# View para processar o formulário (GET mostra, POST salva)
def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save() # grava no banco
            return redirect('lista')
    else:
        form = LivroForm()
    return render(request, 'acervo/form.html', {'form': form})