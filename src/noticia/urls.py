from django.urls import path

from . import views
app_name="noticia"
urlpatterns = [
    path("",views.NoticiaListView.as_view(),name="noticia"),
    path("<int:pk>/", views.NoticiaDetailView.as_view(), name="detail"),
]