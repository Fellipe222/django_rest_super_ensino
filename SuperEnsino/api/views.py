from rest_framework.response import Response
from rest_framework.decorators import api_view
from paginas.models import Pergunta, Alternativa, Aluno, Resposta, Questionario
import json

def compor_pergunta(alternativa,mode='aluno'):
    '''mode: 'aluno' | 'admin' '''
    resultado = {
        'id_pergunta':alternativa.pergunta.id,
        'enunciado':alternativa.pergunta.enunciado,
        'alternativas':{
            'a':alternativa.alternativa_a,
            'b':alternativa.alternativa_b,
            'c':alternativa.alternativa_c,
            'd':alternativa.alternativa_d,
        }
    }
    if mode == 'admin':
        resultado['alternativa_correta'] = alternativa.alternativa_correta
    return resultado

@api_view(['GET'])
def overview(request):
    api_urls = {
        '[ GET ] Visualizar todas perguntas (visão admin)':'/admin/perguntas/',
        '[ GET ] Visualizar todas perguntas (visão aluno)':'/aluno/perguntas/',
        '[ GET ] Visualizar detalhes de uma pergunta (visão admin)':'/admin/perguntas/<str:id_pergunta>/',
        '[ GET ] Visualizar detalhes de uma pergunta (visão aluno)':'/aluno/perguntas/<str:id_pergunta>/',
        '[ GET ] Visualizar desempenho do aluno':'/desempenho/<int:id_aluno>/<int:id_questionario>',
        '[ POST ] Salvar resposta do aluno':'/resposta/<int:id_aluno>'
    }
    return Response(api_urls)

@api_view(['GET'])
def get_perguntas_aluno(request):
    perguntas = Pergunta.objects.all()
    alternativas = Alternativa.objects.filter(pergunta__in=perguntas)
    todas_perguntas = list(map(lambda pergunta: compor_pergunta(pergunta,mode='aluno'),alternativas))
    return Response(todas_perguntas)

@api_view(['GET'])
def get_perguntas_admin(request):
    perguntas = Pergunta.objects.all()
    alternativas = Alternativa.objects.filter(pergunta__in=perguntas)
    todas_perguntas = list(map(lambda pergunta: compor_pergunta(pergunta,mode='admin'),alternativas))
    return Response(todas_perguntas)

@api_view(['GET'])
def get_uma_pergunta_aluno(request, id_pergunta):
    pergunta = Pergunta.objects.get(id=id_pergunta)
    alternativas = Alternativa.objects.get(pergunta=pergunta)
    pergunta = compor_pergunta(alternativas, mode='aluno')
    return Response(pergunta)

@api_view(['GET'])
def get_uma_pergunta_admin(request, id_pergunta):
    pergunta = Pergunta.objects.get(id=id_pergunta)
    alternativas = Alternativa.objects.get(pergunta=pergunta)
    pergunta = compor_pergunta(alternativas, mode='admin')
    return Response(pergunta)

@api_view(['POST'])
def cadastra_resposta(request,id_aluno):
    aluno = Aluno.objects.get(id=id_aluno)
    data = json.loads(request.body)
    pergunta = Pergunta.objects.get(id=data['id_pergunta'])
    valor = data['valor']
    alternativa = Alternativa.objects.get(pergunta=pergunta)
    is_correta = alternativa.verifica_resposta(valor)
    resposta = Resposta.objects.create(aluno=aluno, pergunta=pergunta, valor=valor, is_correta=is_correta)
    return Response({'acertou':is_correta})

@api_view(['GET'])
def get_desempenho_aluno(request,id_aluno, id_questionario):
    def get_resultado(aluno,perguntas:list):
        erros = 0
        acertos = 0
        for pergunta in perguntas:
            resposta = Resposta.objects.get(aluno=aluno,pergunta=pergunta)
            if resposta.is_correta:
                acertos+=1
            elif not resposta.is_correta:
                erros+=1
            else:
                pass
        aproveitamento = round((acertos/len(perguntas)*100),2)
        return {
            'id_aluno':aluno.id,
            'nome_aluno':aluno.nome,
            'questionario':pergunta.questionario.__str__(),
            'acertos':acertos,
            'erros':erros,
            'aproveitamento':f'{aproveitamento}%'
        }
    
    aluno = Aluno.objects.get(id=id_aluno)
    questionario = Questionario.objects.get(id=id_questionario)
    perguntas = list(Pergunta.objects.filter(questionario=questionario))
    resultado = get_resultado(aluno=aluno, perguntas=perguntas)
    return Response(resultado)
