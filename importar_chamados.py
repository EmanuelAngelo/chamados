import pandas as pd
from django.utils import timezone
import os
import django
import pytz

# Configurar o Django - Substitua 'core' pelo nome do seu projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from chamados.models import Chamado, TipoSolicitacao
from django.contrib.auth.models import User

# Definir o fuso horário
tz = pytz.timezone('America/Sao_Paulo')  # Substitua pelo fuso horário correto

# Ler a planilha - Substitua 'caminho/para/sua/planilha.xlsx' pelo caminho real do seu arquivo
df = pd.read_excel(r'D:\Projetos\chamados\PastaChamados.xlsx')

for _, row in df.iterrows():
    tipo_solicitacao, _ = TipoSolicitacao.objects.get_or_create(nome=row['TIPO DE SOLICITAÇÃO/SISTEMA'])
    responsavel, _ = User.objects.get_or_create(username=row['RESPONSAVEL'])

    atribuicao = pd.to_datetime(row['ATRIBUIÇÃO'], dayfirst=True).replace(tzinfo=tz) if pd.notnull(row['ATRIBUIÇÃO']) else None
    conclusao = pd.to_datetime(row['CONCLUSÃO'], dayfirst=True).replace(tzinfo=tz) if pd.notnull(row['CONCLUSÃO']) else None

    Chamado.objects.update_or_create(
        numero=row['NUMERO'],
        defaults={
            'tipo_solicitacao': tipo_solicitacao,
            'responsavel': responsavel,
            'atribuicao': atribuicao,
            'conclusao': conclusao,
            'prioridade': row['PRIORIDADE'],
            'status': row['STATUS'],
            'observacoes': row['OBSERVAÇÕES']
        }
    )
