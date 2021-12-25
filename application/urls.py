from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/freight_forwarding/', views.freight_forwarding, name='freight_forwarding'),
    path('services/storage_transport/', views.storage_transport, name='storage_transport'),
    path('services/warehouse_logistics/', views.warehouse_logistics, name='warehouse_logistics'),
    path('services/removals_relocations/', views.removals_relocations, name='removals_relocations'),
    path('services/project_logistics/', views.project_logistics, name='project_logistics'),
    path('services/logistics_management/', views.logistics_management, name='logistics_management'),
    path('projects/road_project/', views.road_project, name='road_project'),
    path('projects/sea_project/', views.sea_project, name='sea_project'),
    path('projects/railway_project/', views.railway_project, name='railway_project'),
    path('transportation/road_transportation/', views.road_transportation, name='road_transportation'),
    path('transportation/airy_transportation/', views.airy_transportation, name='airy_transportation'),
    path('transportation/sea_transportation/', views.sea_transportation, name='sea_transportation'),
    path('transportation/railway_transportation/', views.railway_transportation, name='railway_transportation'),
    path('contact/', views.contact, name='contact'),
    path('get_quote/', views.get_quote, name='get_quote'),
    path('global_coverage/', views.global_coverage, name='global_coverage'),
]