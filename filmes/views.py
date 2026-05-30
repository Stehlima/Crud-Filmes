from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Filme, Categoria
from .forms import FilmeForm

def listar_filmes(request):
    # Agrupar filmes por categoria
    categorias = Categoria.objects.prefetch_related('filmes').all()
    context = {
        'categorias': categorias
    }
    return render(request, 'filmes/listar_filmes.html', context)

def adicionar_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Filme adicionado com sucesso!')
            return redirect('listar_filmes')
        else:
            messages.error(request, 'Erro ao adicionar filme. Verifique os dados e tente novamente.')
    else:
        form = FilmeForm()
        
    return render(request, 'filmes/form_filme.html', {'form': form, 'acao': 'Adicionar'})

def editar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES, instance=filme)
        if form.is_valid():
            form.save()
            messages.success(request, 'Filme atualizado com sucesso!')
            return redirect('listar_filmes')
    else:
        form = FilmeForm(instance=filme)
        
    return render(request, 'filmes/form_filme.html', {'form': form, 'acao': 'Editar'})

def remover_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == 'POST':
        filme.delete()
        messages.success(request, 'Filme removido com sucesso!')
        return redirect('listar_filmes')
    return render(request, 'filmes/confirmar_exclusao.html', {'filme': filme})
