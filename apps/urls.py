from django.urls import path, include

app_name = 'apps'

urlpatterns = [
    path('', include('apps.core.urls', namespace='core')),
    path('', include('apps.atendimento.urls', namespace='atendimento')),
    path('', include('apps.venda.urls', namespace='venda')),
]
