import datetime
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.db.models import Sum
from apps.venda.models import Compra, ItemCompra
from apps.atendimento.models import Servico, Consulta, ItemServico, ItemConsulta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import now


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
    login_url = "apps:core:login"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["title"] = "Home"
        user = self.request.user
        context["user"] = user

        date = now().date()
        start_week = date - datetime.timedelta(date.weekday())
        end_week = start_week + datetime.timedelta(7)

        context["valor_compras_mes"] = (
            ItemCompra.objects.filter(created_at__month=now().month).aggregate(
                Sum("valor_item")
            )["valor_item__sum"]
            or 0
        )
        context["count_compras_mes"] = Compra.objects.filter(
            created_at__month=now().month
        ).count()
        context["valor_compras_semana"] = (
            ItemCompra.objects.filter(
                created_at__range=[start_week, end_week]
            ).aggregate(Sum("valor_item"))["valor_item__sum"]
            or 0
        )
        # ---------------------------------------
        context["count_compras_semana"] = Compra.objects.filter(
            created_at__range=[start_week, end_week]
        ).count()

        context["valor_servicos_mes"] = sum([servico.valor_servico for servico in Servico.objects.filter(created_at__month=now().month)])
        context["count_servicos_mes"] = Servico.objects.filter(created_at__month=now().month).count()
        context["valor_servicos_semana"] = sum([servico.valor_servico for servico in Servico.objects.filter(created_at__range=[start_week, end_week])])
        context["count_servicos_semana"] = Servico.objects.filter(created_at__range=[start_week, end_week]).count()
        context["valor_consultas_mes"] = sum([consulta.valor_consulta for consulta in Consulta.objects.filter(created_at__month=now().month)])
        context["count_consultas_mes"] = Consulta.objects.filter(created_at__month=now().month).count()
        context["valor_consultas_semana"] = sum([consulta.valor_consulta for consulta in Consulta.objects.filter(created_at__range=[start_week, end_week])])
        context["count_consultas_semana"] = Consulta.objects.filter(created_at__range=[start_week, end_week]).count()

        # List of objects
        context["list_vendas"] = Compra.objects.all().order_by("-id")[:7]
        context["list_servicos"] = Servico.objects.all().order_by("-id")[:7]
        context["list_consultas"] = Consulta.objects.all().order_by("-id")[:7]

        return context
