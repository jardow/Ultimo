from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect

from web.forms import ComentarioForm, ContactoForm
from web.models import Comentario


def comentario(request):
    posts = Comentario.objects.all()
    mi_template = loader.get_template("404.html")
    mi_contexto = Context({'posts': posts})
    return HttpResponse(mi_template.render(mi_contexto))


def inicio(request):
    return render(request, 'index.html')


def acerca(request):
    return render(request, 'about.html')

#conocoto


def conocoto(request):
    return render(request, 'index1.html')


def historia(request):
    return render(request, 'historia.html')


def galeria(request):
    return render(request, 'galeria.html')


def comentarioC(request):
    return render(request, 'comentario.html')


def volar(request):
    if request.method == 'POST':
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/comentario')
    else:
        formulario = ComentarioForm()
        context = {'formulario': formulario}
        return render(request, '404.html', context)


def destino(request):
    return render(request, 'destination.html')


def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje desde el Sitio de Turimo  Web'
            contenido = formulario.cleaned_data['mensaje'] + "\n"
            contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['bacoth@gmail.com'])
            try:
                correo.send()
            except Exception as e:
                print('No fue posible enviar el mensaje, revisar la configuración')
                print(e)
            return HttpResponseRedirect('/')
    else:
        formulario = ContactoForm()
    context = {'formulario': formulario}
    return render(request, 'contact.html', context)
