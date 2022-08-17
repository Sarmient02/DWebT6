from xml.dom.minidom import Document
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .forms import DocumentosForm

from .models import TipoDocumento


# Create your views here.

def index(request):
    documentos = TipoDocumento.objects.all()
    template = loader.get_template('persona/index.html')
    context = {
        'documentos':documentos,
    }
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context,request))

def documentos(request):
    documentos = TipoDocumento.objects.all()
    template = loader.get_template('persona/documentos.html')
    context = {
        'documentos':documentos,
    }
    return HttpResponse(template.render(context, request))

def new_document(request):

    if request.method == 'POST':

        form = DocumentosForm(request.POST)

        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            doc = TipoDocumento(nombre=nombre,descripcion=descripcion)
            doc.save()
            return HttpResponseRedirect(reverse('documentos'))

    else:
            form = DocumentosForm()

    return render(request, 'persona/create_documentos.html', {'form':form})

