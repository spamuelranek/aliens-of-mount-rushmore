from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Alien
from django.urls import reverse_lazy

class AlienListView(ListView):
  template_name = "aliens/alien_list.html"
  model = Alien 

class AlienDetailView(DetailView):
  teplate_name = "aliens/alien_detail.html"
  model = Alien

class AlienCreatView(CreateView):
  template_name = "aliens/alien_create.html"
  model = Alien
  fields = ["reporter","given_name_of_subject", "species", "number_of_apendages", "number_of_eyes", "description", "risk_level"]

class AlienUpdateView(UpdateView):
  template_name = "aliens/alien_update.html"
  model = Alien
  fields = ["given_name_of_subject", "species", "number_of_apendages", "number_of_eyes","description"]

class AlienDeleteView(DeleteView):
  template_name = "aliens/alien_delete.html"
  model = Alien
  success_url = reverse_lazy("aliens/alien_list")
