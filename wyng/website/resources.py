from import_export import resources
from .models import prod_mst, whs_mst,stg_mst,whs_inventory,stg_inventory,whs_stg, Person, replenishment, required_qty

class prodMstResource(resources.ModelResource):
    class Meta:
        model = prod_mst

class whsMstResource(resources.ModelResource):
    class Meta:
        model = whs_mst

class stgMstResource(resources.ModelResource):
    class Meta:
        model = stg_mst
        exclude = ('id',)

class whsInventoryResource(resources.ModelResource):
    class Meta:
        model = whs_inventory

class stgInventoryResource(resources.ModelResource):
    class Meta:
        model = stg_inventory

class whsStgResource(resources.ModelResource):
    class Meta:
        model = whs_stg

class replenishmentResource(resources.ModelResource):
    class Meta:
        model = replenishment

class required_qtyResource(resources.ModelResource):
    class Meta:
        model = required_qty