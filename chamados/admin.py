# chamados/admin.py

from django.contrib import admin
from .models import Chamado, TipoSolicitacao

class ChamadoAdmin(admin.ModelAdmin):
    list_display = ['numero', 'tipo_solicitacao', 'responsavel', 'atribuicao', 'conclusao', 'tempo', 'prioridade', 'status', 'observacoes']
    list_filter = ['prioridade', 'status', 'tipo_solicitacao']
    search_fields = ['numero', 'responsavel__username', 'tipo_solicitacao__nome']
    list_per_page = 15

admin.site.register(Chamado, ChamadoAdmin)
admin.site.register(TipoSolicitacao)
