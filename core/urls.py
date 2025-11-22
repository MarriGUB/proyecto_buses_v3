from django.urls import path
from . import views

urlpatterns = [
    # Conductores
    path('conductores/', views.ConductorListView.as_view(), name='conductor_list'),
    path('conductores/nuevo/', views.ConductorCreateView.as_view(), name='conductor_create'),
    path('conductores/<int:pk>/', views.ConductorDetailView.as_view(), name='conductor_detail'),
    path('conductores/<int:pk>/editar/', views.ConductorUpdateView.as_view(), name='conductor_update'),
    path('conductores/<int:pk>/eliminar/', views.ConductorDeleteView.as_view(), name='conductor_delete'),
    
    # Lugares
    path('lugares/', views.LugarListView.as_view(), name='lugar_list'),
    path('lugares/nuevo/', views.LugarCreateView.as_view(), name='lugar_create'),
    path('lugares/<int:pk>/', views.LugarDetailView.as_view(), name='lugar_detail'),
    path('lugares/<int:pk>/editar/', views.LugarUpdateView.as_view(), name='lugar_update'),
    path('lugares/<int:pk>/eliminar/', views.LugarDeleteView.as_view(), name='lugar_delete'),
    
    # Pasajeros
    path('pasajeros/', views.PasajeroListView.as_view(), name='pasajero_list'),
    path('pasajeros/nuevo/', views.PasajeroCreateView.as_view(), name='pasajero_create'),
    path('pasajeros/<int:pk>/', views.PasajeroDetailView.as_view(), name='pasajero_detail'),
    path('pasajeros/<int:pk>/editar/', views.PasajeroUpdateView.as_view(), name='pasajero_update'),
    path('pasajeros/<int:pk>/eliminar/', views.PasajeroDeleteView.as_view(), name='pasajero_delete'),
]
