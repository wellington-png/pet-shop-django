from apps.core.views.home import HomeView
from apps.core.views.login import LoginView
from apps.core.views.logout import LogoutView
from apps.core.views.pet import PetCreateView, PetListView, PetUpdateView, PetDeleteView
from apps.core.views.cliente import (
    ClienteCreateView,
    ClienteListView,
    ClienteUpdateView,
    ClienteDeleteView,
)


__all__ = [
    "HomeView",
    "LoginView",
    "LogoutView",
    "PetCreateView",
    "PetListView",
    "PetUpdateView",
    "PetDeleteView",
    "ClienteCreateView",
    "ClienteListView",
    "ClienteUpdateView",
    "ClienteDeleteView",
]
