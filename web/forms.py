# This Python file uses the following encoding: utf-8
from django.forms import ModelForm
from django import forms
from .models import Comentario


class ContactoForm(forms.Form):
    correo = forms.EmailField(label='Tú correo electrónico')
    mensaje = forms.CharField(widget=forms.Textarea)


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
