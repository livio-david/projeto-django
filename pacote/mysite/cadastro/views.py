from django.shortcuts import render
from django.http import HttpResponse
from .forms import formularioPessoa
from .models import pessoas

def inicio(request):
    return render(request, 'cadastro/inicio.html')


def cadastrar(request):
    form = formularioPessoa(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'cadastro/cadastradas.html', {'form': form})
    else:
        form = formularioPessoa()
        return render(request, 'cadastro/cadastrar.html', {'form': form})

def cadastradas(request):
    context ={}
    context["dataset"] = pessoas.objects.all()
    return render(request, "cadastro/cadastradas.html", context)
    

