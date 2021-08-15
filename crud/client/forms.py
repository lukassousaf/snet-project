from django import forms
from localflavor.br.forms import BRZipCodeField


class ClientForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    cell = forms.CharField(label='Telefone', max_length=11)
    cep = BRZipCodeField(label='CEP', max_length=9)
    rua = forms.CharField(label='Rua', max_length=100)
    bairro = forms.CharField(label='Bairro', max_length=100)
    cidade = forms.CharField(label='Cidade', max_length=100)
    estado = forms.CharField(label='Estado', max_length=100)
    num = forms.CharField(label='Número', max_length=5)
