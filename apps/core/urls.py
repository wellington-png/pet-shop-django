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
    value_week,
)

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("clientes/create/", ClienteCreateView.as_view(), name="cliente_create"),
    path("clientes/", ClienteListView.as_view(), name="cliente_list"),
    path(
        "clientes/update/<int:pk>/", ClienteUpdateView.as_view(), name="cliente_update"
    ),
    path(
        "clientes/delete/<int:pk>/", ClienteDeleteView.as_view(), name="cliente_delete"
    ),
    path("pets/create/", PetCreateView.as_view(), name="pet_create"),
    path("pets/", PetListView.as_view(), name="pet_list"),
    path("pets/update/<int:pk>/", PetUpdateView.as_view(), name="pet_update"),
    path("pets/delete/<int:pk>/", PetDeleteView.as_view(), name="pet_delete"),
    path("value_week/", value_week, name="value_week"),
]
