from django.shortcuts import render
from base.forms import ContatoForm, InscreverForm
from base.models import Contato
from eventos.models import Categoria


def inicio(request):
    dados = []
    dados.append(
        {
            'titulo': 'Titulo 1',
            'categoria': 'Categoria 1',
            'data': '28/06/2023',
        }
    )
    dados.append(
        {
            'titulo': 'Titulo 2',
            'categoria': 'Categoria 2',
            'data': '27/06/2023',
        }
    )
    contexto = {
        'dados': dados,
    }
    resposta = render(request, 'inicio.html', contexto)
    return resposta


def inscrever(request):
    contexto = {'sucesso': False}
    form = InscreverForm(request.POST or None)
    if form.is_valid():
        form.save()
        contexto['sucesso'] = True
    contexto['form'] = form
    return render(request, 'inscrever.html', contexto)


def contato(request):
    sucesso = False
    if request.method == 'GET':
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            sucesso = True
    contexto = {
        'telefone': '(99) 99999.9999',
        'responsavel': 'Maria da Silva Pereira',
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'contato.html', contexto)

# Toda view precisa receber um primeiro parâmetro chamado request.
# Esse objeto irá conter informações sobre a requisição atual
# (as informações que o navegador repassa ao servidor) e,
# para que ela seja acessada pelos usuários,
# é preciso criar uma rota ou url que, ao ser acessada, ative-a.
# Para isso, vamos precisar alterar o arquivo urls.py,
# que está dentro da pasta ultima (no mesmo diretório do arquivo settings.py)
