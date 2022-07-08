from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Estagio
from .form import PostarModelForm
import uuid
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

def index(request):
    files = Estagio.objects.all().order_by("-id")
    return render(request, 'estagio/index.html', {'files': files})


# Create your views here.
@login_required
@permission_required('estagio.est')
def postar(request):
    if request.method == "POST":
        form = PostarModelForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.criado_por = request.user
            form.save()
            return redirect("/estagio/")
    else:
        form = PostarModelForm()

    return render(request, 'estagio/upload_form.html', {'form': form, 'heading': 'Postar documentos de estágio'})


# file path relative to 'media' folder
def handle_uploaded_file(file):
    ext = file.name.split('.')[-1]
    file_name = '{}.{}'.format(uuid.uuid4().hex[:10], ext)

    file_path = os.path.join('files', file_name)
    absolute_file_path = os.path.join('media', 'files', file_name)

    directory = os.path.dirname(absolute_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(absolute_file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return file_path

@login_required
@permission_required('estagio.exc')
def excluir(request, id):
    
    Estagio.objects.get(pk=id).delete()
    
    return HttpResponseRedirect("/estagio/")

@login_required
@permission_required('estagio.ed')
def editar(request, id):
    file = Estagio.objects.get(pk=id)
    form = PostarModelForm(instance=file)
    
    if request.method == "POST":
        form = PostarModelForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/estagio/")
    else:    
        form = PostarModelForm(instance=file)
    
    context = {
        'form': form,
        'file': file
    }
    
    return render(request, 'estagio/formEdit.html', context)

def detail(request, id):
    estagio = Estagio.objects.get(pk=id)
    context = {
        'estagio': estagio
    }
    
    return render(request, 'estagio/detail.html', context)

def template(request):
    return render(request, 'index.html', {})


@login_required
def publicar(request):
    list_filter = Estagio.objects.order_by('titulo').filter(postar=True)
    
    if 'publicar' in request.GET:
        nome = request.GET['publicar']
        if nome:
            list_filter = list_filter.filter(titulo__icontains=nome)

    return render(request, 'estagio/publicar.html', {'files': list_filter})
