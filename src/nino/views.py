from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import NNA
# Create your views here.


class NNAListView(generic.ListView):
    model = NNA
    template_name = "list.html"


class NNADetailView(generic.DetailView):
    model = NNA
    template_name = "detail.html"

def calendario(request):
    return render(request, 'calendario.html')