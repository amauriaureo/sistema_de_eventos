from django import forms
from base.models import Contato


class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)


class InscreverForm(forms.ModelForm):

    class Meta:
        model = Contato
        fields = [
            'nome',
            'email',
            'preferencia_evento',
            'observacao',
        ]
