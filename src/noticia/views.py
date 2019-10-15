from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Noticia
# Create your views here.

class NoticiaListView(generic.ListView):
    model = Noticia
    template_name = "noticia.html"


class NoticiaDetailView(generic.DetailView):
    model = Noticia
    template_name = "detail.html"

