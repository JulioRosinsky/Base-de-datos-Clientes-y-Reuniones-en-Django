from django.forms import ModelForm
from .models import *

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre', 
            'apellido', 
            'fecha_de_nacimiento',
            'ejecutivo',
            'familia',
            'direcion',
            'activo',
            'relevancia',
            ]
        
class ReunionesForm(ModelForm):
    class Meta:
        model = Reuniones
        fields = [
            'titulo',
            'fecha',
            'situacion',
            'ejecutivo',
            'cliente',
            'comentario',
            'archivo',
        ]
        
class FamiliaForm(ModelForm):
    class Meta:
        model = Familia
        fields = [
            'nombre',
        ]
        
class SociedadesForm(ModelForm):
    class Meta:
        model = Sociedades
        fields = [
            'nombre',
            'familia',
        ]