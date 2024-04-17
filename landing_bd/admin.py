from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(Cliente)
class ClienteAdmin(ImportExportModelAdmin):
    pass

@admin.register(Familia)
class FamiliaAdmin(ImportExportModelAdmin):
    pass

@admin.register(Sociedades)
class SociedadesAdmin(ImportExportModelAdmin):
    pass

@admin.register(Reuniones)
class ReunionesAdmin(ImportExportModelAdmin):
    pass
