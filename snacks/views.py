from django.shortcuts import render
from snacks.models import Snack
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy


# from .models import Snack
# Create your views here.

class SnacksListView(ListView):
    template_name = 'snacks_t/snack_list.html'
    model = Snack


class SnacksDetailView(DetailView):
    template_name = "snacks_t/snacks_detail.html"
    model = Snack


class SnackCreateView(CreateView):
    template_name = "snacks_t/Create.html"
    model = Snack
    fields = ["title","discribtion","purchaser"]


class SnackUpdateView(UpdateView):
    template_name = 'snacks_t/update.html'
    model = Snack
    fields = ["title","discribtion","purchaser"]


class SnackDeleteView(DeleteView):
    template_name = 'snacks_t/delete.html'
    model = Snack
    success_url = reverse_lazy("home")
