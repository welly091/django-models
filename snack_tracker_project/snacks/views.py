from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Snack, Drink

# Create your views here.
class ShowListView(ListView):
    template_name = "snack_list.html"
    model = Snack

class ShowDetailListView(DetailView):
    template_name = "snack_detail.html"
    model = Snack

class ShowDrinkView(ListView):
    template_name = "drink_list.html"
    model = Drink

class ShowDetailDrinkView(DetailView):
    template_name = "drink_detail.html"
    model = Drink