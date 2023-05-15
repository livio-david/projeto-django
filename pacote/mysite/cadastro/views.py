from django.shortcuts import render
from django.http import HttpResponse
from  .forms import formularioPessoa

def inicio(request):
    return render(request, 'cadastro/inicio.html')


def cadastrar(request):
    form = formularioPessoa(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse('salvo com sucesso')
    return render(request, 'cadastro/cadastrar.html', {'form': form})

def cadastradas(request):
    form = formularioPessoa(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse('salvo com sucesso')
    return HttpResponse(form)
