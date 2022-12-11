from django.urls import path


from apps.core.views import HomeView, LoginView, LogoutView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
