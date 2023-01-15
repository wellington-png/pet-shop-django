from django.urls import path

from apps.account.views import (
    TecnicoCreateView,
    TecnicoListView,
    TecnicoUpdateView,
    TecnicoDeleteView,
    VeterinarioCreateView,
    VeterinarioListView,
    VeterinarioUpdateView,
    VeterinarioDeleteView,
    AtendenteCreateView,
    AtendenteListView,
    AtendenteUpdateView,
    AtendenteDeleteView,
)

app_name = "account"

urlpatterns = [
    path("tecnico/list/", TecnicoListView.as_view(), name="tecnico_list"),
    path("tecnico/create/", TecnicoCreateView.as_view(), name="tecnico_create"),
    path(
        "tecnico/update/<int:pk>/", TecnicoUpdateView.as_view(), name="tecnico_update"
    ),
    path(
        "tecnico/delete/<int:pk>/", TecnicoDeleteView.as_view(), name="tecnico_delete"
    ),
    path("veterinario/list/", VeterinarioListView.as_view(), name="veterinario_list"),
    path(
        "veterinario/create/",
        VeterinarioCreateView.as_view(),
        name="veterinario_create",
    ),
    path(
        "veterinario/update/<int:pk>/",
        VeterinarioUpdateView.as_view(),
        name="veterinario_update",
    ),
    path(
        "veterinario/delete/<int:pk>/",
        VeterinarioDeleteView.as_view(),
        name="veterinario_delete",
    ),
    path("atendente/list/", AtendenteListView.as_view(), name="atendente_list"),
    path("atendente/create/", AtendenteCreateView.as_view(), name="atendente_create"),
    path(
        "atendente/update/<int:pk>/",
        AtendenteUpdateView.as_view(),
        name="atendente_update",
    ),
    path(
        "atendente/delete/<int:pk>/",
        AtendenteDeleteView.as_view(),
        name="atendente_delete",
    ),
]
