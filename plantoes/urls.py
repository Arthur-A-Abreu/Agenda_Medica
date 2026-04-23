from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendario_view, name='calendario'),
    path('atualizar/', views.atualizar_plantao, name='atualizar_plantao'),
    path('excluir/', views.excluir_plantao, name='excluir_plantao'),
    path('status/', views.mudar_status_plantao, name='mudar_status_plantao'),
    path('solicitar-troca/', views.solicitar_troca, name='solicitar_troca'),
    path('gerenciar-trocas/', views.gerenciar_trocas, name='gerenciar_trocas'),
    path('responder-troca/<int:troca_id>/', views.responder_troca, name='responder_troca'),
    path('historico/', views.historico_mudancas, name='historico_mudancas'),
]
