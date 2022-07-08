from atexit import register
from django.contrib import admin

from .models import Post

class ListandoPost(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',) # Busca num campo no topo.
    list_filter = ('title', ) # Filtros em um painel à direita.
   
    

admin.site.register(Post, ListandoPost)
