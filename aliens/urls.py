from django.urls import path
from .views import AlienCreatView, AlienDeleteView, AlienDetailView, AlienListView, AlienUpdateView


urlpatterns = [
  path("",AlienListView.as_view(), name = "alien_list"),
  path("<int:pk>/",AlienDetailView.as_view(), name = "alien_detail"),
  path("create/", AlienCreatView.as_view(), name = "alien_create"),
  path("<int:pk>/delete/", AlienDeleteView.as_view(), name = "alien_delete"),
  path("<int:pk>/update/", AlienUpdateView.as_view(), name = "alien_update"),
]