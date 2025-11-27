from django.urls import path
from . import views

app_name = 'viajes'

urlpatterns = [
    # Viajes
    path('', views.ViajeListView.as_view(), name='viaje_list'),
    path('nuevo/', views.ViajeCreateView.as_view(), name='viaje_create'),
    path('<int:pk>/', views.ViajeDetailView.as_view(), name='viaje_detail'),
    path('<int:pk>/editar/', views.ViajeUpdateView.as_view(), name='viaje_update'),
    path('<int:pk>/eliminar/', views.ViajeDeleteView.as_view(), name='viaje_delete'),
    
    # Gestión de pasajeros en viajes
    path('<int:pk>/pasajeros/', views.viaje_pasajeros_view, name='viaje_pasajeros'),
    path('<int:pk>/pasajeros/agregar/', views.agregar_pasajero_viaje, name='agregar_pasajero_viaje'),
    path('<int:pk>/pasajeros/<int:pasajero_pk>/quitar/', views.quitar_pasajero_viaje, name='quitar_pasajero_viaje'),
    path('<int:pk>/pasajeros/<int:pasajero_pk>/editar/', views.editar_pasajero_viaje, name='editar_pasajero_viaje'),
    
    # NUEVA URL PARA ITINERARIO
    path('<int:pk>/itinerario/', views.itinerario_view, name='itinerario'),
    
    # Gestión de costos del viaje
    path('<int:pk>/costos/', views.gestion_costos_view, name='gestion_costos'),
]