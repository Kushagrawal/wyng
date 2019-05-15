from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('fileup/', views.simple_upload, name = 'simple_upload'),
    path('whsstg/', views.whs_stg_upload, name = 'whs_stg_upload'),
    path('prodmst/', views.product_mst_upload, name = 'prod_mst'),
    path('stgmst/', views.storage_mst_upload, name = 'storage_mst'),
    path('stginv/', views.stg_inventory_upload, name = 'stg_inventory'),
    path('whsinv/', views.whs_inventory_upload, name = 'whs_inventory'),
    path('whsmst/', views.whs_mst_upload, name = 'whs_mst'),
    path('exportrepl/', views.exportrepl, name = 'exportrepl'),
    path('exportreqd/', views.exportreqd, name = 'exportreqd'),

]