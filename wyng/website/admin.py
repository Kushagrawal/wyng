from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import prod_mst,whs_mst, stg_mst, whs_stg, whs_inventory, stg_inventory, Person

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(prod_mst)
class ViewAdmin(ImportExportModelAdmin):
    pass

admin.site.register(whs_mst)
admin.site.register(stg_mst)
admin.site.register(whs_stg)
admin.site.register(whs_inventory)
admin.site.register(stg_inventory)
# Register your models here.
