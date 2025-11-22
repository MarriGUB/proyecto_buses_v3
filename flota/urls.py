from django.urls import path
from . import views

app_name = 'flota'  # Namespace para las URLs

urlpatterns = [
    # Buses - Proyecto Principal
    path('buses/', views.BusListView.as_view(), name='bus_list'),
    path('buses/nuevo/', views.BusCreateView.as_view(), name='bus_create'),
    path('buses/<int:pk>/', views.BusDetailView.as_view(), name='bus_detail'),
    path('buses/<int:pk>/editar/', views.BusUpdateView.as_view(), name='bus_update'),
    path('buses/<int:pk>/eliminar/', views.BusDeleteView.as_view(), name='bus_delete'),
    
    # Mantenimientos - Del código de patentes
    path('buses/<int:bus_id>/mantenimiento/crear/', views.MantenimientoCreateView.as_view(), name='mantenimiento_crear'),
    path('mantenimiento/<int:pk>/editar/', views.MantenimientoUpdateView.as_view(), name='mantenimiento_editar'),
    path('mantenimiento/<int:pk>/eliminar/', views.MantenimientoDeleteView.as_view(), name='mantenimiento_eliminar'),
    
    # Documentos Vehiculares - Del código de patentes
    path('buses/<int:bus_id>/documento/crear/', views.DocumentoVehiculoCreateView.as_view(), name='documento_crear'),
    path('documento/<int:pk>/editar/', views.DocumentoVehiculoUpdateView.as_view(), name='documento_editar'),
    path('documento/<int:pk>/eliminar/', views.DocumentoVehiculoDeleteView.as_view(), name='documento_eliminar'),
]