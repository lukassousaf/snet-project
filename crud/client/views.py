import re
from .models import *
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.forms import ModelForm
from .forms import ClientForm
from django.shortcuts import get_object_or_404, redirect, render


class ClientFormView(FormView):
    form_class = ClientForm
    success_url = reverse_lazy('client:client')
    template_name = 'client/client.html'

# class BaseeView(ListView):
#     queryset = [str(user) for user in User.objects.filter(username)]
#     template_name= 'basee.html'


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['nome', 'telefone', 'cep', 'rua',
                  'bairro', 'cidade', 'estado', 'numero']


def client_list(request, template_name='client_list.html'):
    client = Client.objects.all()
    clients = {'lista': client}
    return render(request, template_name, clients)


def client_new(request, template_name="client_form.html"):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('client:client_list')
    return render(request, template_name, {'form': form})


def client_edit(request, pk, template_name='client_form.html'):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save()
            return redirect('client:client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, template_name, {'form': form})


def client_remove(request, pk):
    client = Client.objects.get(pk=pk)
    if request.method == "POST":
        client.delete()
        return redirect('client:client_list')
    return render(request, 'client_delete.html', {'client': client})
