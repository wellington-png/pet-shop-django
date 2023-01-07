from django.urls import path


from apps.core.views import (
    HomeView,
    LoginView,
    LogoutView,
    ClienteCreateView,
    ClienteListView,
    ClienteUpdateView,
    ClienteDeleteView,
    PetCreateView,
    PetListView,
    PetUpdateView,
    PetDeleteView,
)

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("clientes/create/", ClienteCreateView.as_view(), name="cliente_create"),
    path("clientes/", ClienteListView.as_view(), name="cliente_list"),
    path("clientes/update/", ClienteUpdateView.as_view(), name="cliente_update"),
    path("clientes/delete/", ClienteDeleteView.as_view(), name="cliente_delete"),
    path("pets/create/", PetCreateView.as_view(), name="pet_create"),
    path("pets/", PetListView.as_view(), name="pet_list"),
    path("pets/update/", PetUpdateView.as_view(), name="pet_update"),
    path("pets/delete/", PetDeleteView.as_view(), name="pet_delete"),
]
