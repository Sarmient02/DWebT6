from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('persona/', views.index, name='index'),
    path('documentos/', views.documentos, name='documentos'),
    path('documentos/new/', views.new_document, name='new_document'),
]