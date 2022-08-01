from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name='overview'),

    path('aluno/perguntas/', views.get_perguntas_aluno, name='perguntas-aluno'),
    path('admin/perguntas/', views.get_perguntas_admin, name='perguntas-admin'),

    path('aluno/perguntas/<int:id_pergunta>/', views.get_uma_pergunta_aluno, name='detalhes-pergunta-aluno'),
    path('admin/perguntas/<int:id_pergunta>/', views.get_uma_pergunta_admin, name='detalhes-pergunta-admin'),

    path('resposta/<int:id_aluno>', views.cadastra_resposta, name='resposta'),
    path('desempenho/<int:id_aluno>/<int:id_questionario>', views.get_desempenho_aluno, name='desempenho'),
    ]
