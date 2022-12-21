from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
import copy


class LoginView(View):
    template_name = "login.html"


    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username or not password:
            print('Usuário e senha são obrigatórios.')
            messages.error(
                self.request,
                'Usuário e senha são obrigatórios.'
            )
            return redirect('apps:core:login')

        usuario = authenticate(self.request, username=username, password=password)

        if not usuario:
            print('Usuário ou senha inválidos.')
            messages.error(
                self.request,
                'Usuário ou senha inválidos.'
            )
            return redirect('apps:core:login')

        login(self.request, user=usuario)

        messages.success(
            self.request,
            'Você fez login no sistema e pode concluir sua compra.'
        )
        return redirect('apps:core:home')

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

    