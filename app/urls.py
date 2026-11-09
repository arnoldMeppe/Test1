from django.urls import path
from .views import generer_pv

urlpatterns = [
    path('', generer_pv, name='generer_pv'),
]

