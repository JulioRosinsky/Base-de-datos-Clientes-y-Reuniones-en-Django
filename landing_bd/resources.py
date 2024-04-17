from import_export import resources
from .models import *

from import_export import resources, fields
from import_export.widgets import DateWidget
from .models import Cliente

class ClienteResource(resources.ModelResource):
    fecha_de_nacimiento = fields.Field(
        column_name='fecha_de_nacimiento',
        attribute='fecha_de_nacimiento',
        widget=DateWidget(format='%d/%m/%Y')
    )

    class Meta:
        model = Cliente
        fields = ('id', 'nombre', 'apellido', 'fecha_de_nacimiento', 'ejecutivo', 'familia', 'direcion', 'activo', 'relevancia')
        import_id_fields = ['id'] 
        
class ReunionesResource(resources.ModelResource):
    class Meta:
        model = Reuniones
        