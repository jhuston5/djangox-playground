# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Drill
from django.urls import reverse_lazy


class DrillListView(ListView):
  template_name="drill_list.html"
  model = Drill
  context_object_name = 'drill'

class DrillDetailView(DetailView):
  template_name = "drill_detail.html"
  model = Drill

class DrillCreateView(CreateView):
  template_name = "drill_create.html"
  model = Drill
  fields = ['drill_date', 'soldier', 'location', 'description']

class DrillUpdateView(UpdateView):
  template_name = "drill_update.html"
  model = Drill
  fields = ['drill_date', 'soldier', 'location', 'description']

class DrillDeleteView(DeleteView):
  template_name = "drill_delete.html"
  model = Drill
  success_url = reverse_lazy('drill_list')
