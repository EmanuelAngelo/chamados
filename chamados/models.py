from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TipoSolicitacao(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Chamado(models.Model):
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
    ]

    numero = models.CharField(max_length=50, unique=True)
    tipo_solicitacao = models.ForeignKey(TipoSolicitacao, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)
    atribuicao = models.DateTimeField(null=True, blank=True)
    conclusao = models.DateTimeField(null=True, blank=True)
    prioridade = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    observacoes = models.TextField()

    def calcular_tempo(self):
        if self.conclusao:
            return self.conclusao - self.atribuicao
        return None

    @property
    def tempo(self):
        return self.calcular_tempo()

    def __str__(self):
        return f'Chamado {self.numero} - {self.tipo_solicitacao}'

    class Meta:
        verbose_name_plural = 'Chamados'
