from django.urls import path
from playground import views
#from playground.views import curso
#from playground.admin import admin

urlpatterns = [
    path('',views.inicial),
    path('curso', views.curso, name="curso"),
    path('profesores', views.profesores),
    path('estudiantes', views.estudiantes),
    path('entregables', views.entregables),


]

