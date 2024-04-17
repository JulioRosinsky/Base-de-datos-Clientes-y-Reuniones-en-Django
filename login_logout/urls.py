from . import views
from django.urls import path
from .views import user_login, user_signup, cerrar_sesion

urlpatterns = [
    path('', user_login, name="login"),
    path('crea_tu_cuenta/', user_signup, name="crear"),
    path('cerrar_sesion/', cerrar_sesion, name="cerrar_sesion"),
]
