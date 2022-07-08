from django.contrib import admin

from .models import Auxilio


class ListandoAuxilio(admin.ModelAdmin):
    # Opções disponíveis em https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#modeladmin-options
    list_display = ('id', 'titulo')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',) # Busca num campo no topo.
    list_filter = ('titulo',) # Filtros em um painel à direita.
    
admin.site.register(Auxilio, ListandoAuxilio)
