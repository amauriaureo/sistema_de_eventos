"""ultima URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from base.views import inicio, contato, inscrever

from eventos.views import evento

urlpatterns = [
    path('', inicio, name='inicio'),
    path('inscreva-se/', inscrever, name='inscrever'),
    path('contato/', contato, name='contato'),
    path('eventos/<int:id>', evento, name='evento'),
    path('admin/', admin.site.urls),
]

# No código acima, fizemos a importação da função inicio na linha 19 e,
# em seguida, adicionamos uma nova url/rota (linha 22).
# Para adicionar uma nova rota, usamos a função path.
# Ela recebe como primeiro parâmetro o endereço do link que, neste caso,
# deixamos vazio porque é a página inicial e, no segundo parâmetro,
# inserimos o nome da função que será executada
# (a função é passada como parâmetro).
