from django.contrib import admin
from bikes.models import Produto


class ListandoBikes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ano', 'publicada')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('ano', 'usuario',)
    list_per_page = 10
    list_editable = ('publicada',)


admin.site.register(Produto, ListandoBikes)

