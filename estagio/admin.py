from django.contrib import admin

from .models import Estagio

class ListandoEstagio(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',) # Busca num campo no topo.
    list_filter = ('titulo', ) # Filtros em um painel à direita.
   

admin.site.register(Estagio, ListandoEstagio)
