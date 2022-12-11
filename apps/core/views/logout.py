from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import  logout


class LogoutView(View):
    template_name = "login.html"

    def get(self, *args, **kwargs):
        logout(self.request)
        messages.success(
            self.request,
            'Você fez logout no sistema.'
        )
        return redirect('apps:core:login')

    def post(self, *args, **kwargs):
        return render(self.request, self.template_name)
