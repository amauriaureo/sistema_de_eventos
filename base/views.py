from django.shortcuts import render
from django.http import HttpResponse


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
        'dados': dados
    }
    resposta = render(request, 'inicio.html', contexto)
    return resposta


def contato(request):
    return render(request, 'contato.html')

# Toda view precisa receber um primeiro parâmetro chamado request.
# Esse objeto irá conter informações sobre a requisição atual
# (as informações que o navegador repassa ao servidor) e,
# para que ela seja acessada pelos usuários,
# é preciso criar uma rota ou url que, ao ser acessada, ative-a.
# Para isso, vamos precisar alterar o arquivo urls.py,
# que está dentro da pasta ultima (no mesmo diretório do arquivo settings.py)
