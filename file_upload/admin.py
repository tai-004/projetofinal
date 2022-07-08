from atexit import register
from django.contrib import admin

from .models import File

class ListandoFile(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'orientador', 'turma')
    list_display_links = ('id', 'titulo',  'orientador', 'turma')
    search_fields = ('titulo',  'orientador', 'turma') # Busca num campo no topo.
    list_filter = ('titulo', 'orientador', 'turma' ) # Filtros em um painel à direita.
   
    
admin.site.register(File, ListandoFile)

