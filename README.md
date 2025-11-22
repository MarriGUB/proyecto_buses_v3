# Sistema de Gestión de Flota de Buses

## Descripción
Sistema web desarrollado en Django para la gestión integral de una flota de buses, incluyendo la administración de buses, conductores, lugares y viajes.

## Características Implementadas

### ✅ CRUD de Buses
- **Listar buses**: Visualización de todos los buses con información clave
- **Agregar bus**: Formulario completo para registrar nuevos buses
- **Ver detalles**: Vista detallada con información completa del bus
- **Editar bus**: Modificación de datos existentes
- **Eliminar bus**: Confirmación de eliminación con advertencias

### ✅ CRUD de Conductores
- **Listar conductores**: Vista de todos los conductores registrados
- **Agregar conductor**: Formulario para nuevos conductores
- **Ver detalles**: Información completa del conductor con estadísticas
- **Editar conductor**: Actualización de datos del conductor
- **Eliminar conductor**: Eliminación con confirmación

### ✅ CRUD de Lugares
- **Listar lugares**: Visualización de lugares con coordenadas
- **Agregar lugar**: Formulario con soporte para coordenadas GPS
- **Ver detalles**: Vista con información geográfica
- **Editar lugar**: Modificación de información del lugar
- **Eliminar lugar**: Eliminación con advertencias

### ✅ CRUD de Viajes
- **Listar viajes**: Visualización de todos los viajes programados y completados
- **Agregar viaje**: Formulario completo para registrar nuevos viajes
- **Ver detalles**: Información completa del viaje con coordenadas de origen y destino
- **Editar viaje**: Actualización de información del viaje
- **Eliminar viaje**: Eliminación con confirmación
- **Captura automática de coordenadas**: Las coordenadas se guardan automáticamente desde los lugares de origen y destino

### ✅ Interfaz de Usuario
- **Diseño responsivo**: Compatible con dispositivos móviles y desktop
- **Bootstrap 5**: Interfaz moderna y profesional
- **Font Awesome**: Iconografía completa
- **Navegación intuitiva**: Sidebar con navegación clara
- **Mensajes de feedback**: Confirmaciones y errores claros

## Tecnologías Utilizadas
- **Backend**: Django 5.2.8
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Base de datos**: MySQL
- **Iconos**: Font Awesome 6
- **Estilos**: Bootstrap + CSS personalizado

## Instalación y Configuración

### Prerrequisitos
- Python 3.8+
- MySQL Server
- Git

### Pasos de instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd proyecto_flota_buses-main-mockup-4-cristofer-y-juan
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows
   # source venv/bin/activate  # En Linux/Mac
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar base de datos**
   - Crear base de datos MySQL llamada `sistema_gestion_buses`
   - Verificar credenciales en `sistema_flota/settings.py`

5. **Ejecutar migraciones**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crear superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Iniciar servidor**
   ```bash
   python manage.py runserver
   ```

### Inicio rápido con script
Para Windows, puedes usar el script automatizado:
```bash
iniciar_sistema.bat
```

## Estructura del Proyecto

```
proyecto_flota_buses/
├── core/                   # App principal (conductores, lugares)
│   ├── models.py          # Modelos Conductor y Lugar
│   ├── views.py           # Vistas CRUD
│   ├── urls.py            # URLs de core
│   ├── admin.py           # Admin de Django
│   └── migrations/
├── flota/                 # App de gestión de buses
│   ├── models.py          # Modelos Bus, Documento, Mantenimiento
│   ├── views.py           # Vistas CRUD de buses
│   ├── urls.py            # URLs de flota
│   ├── admin.py           # Admin de Django
│   └── migrations/
├── viajes/                # App de gestión de viajes
│   ├── models.py          # Modelo Viaje
│   ├── views.py           # Vistas CRUD de viajes
│   ├── urls.py            # URLs de viajes
│   ├── admin.py           # Admin de Django
│   └── migrations/
├── costos/                # App de costos
│   ├── models.py          # Modelos de costos
│   ├── views.py           # Vistas
│   ├── urls.py            # URLs de costos
│   └── migrations/
├── templates/             # Plantillas HTML
│   ├── base.html          # Plantilla base
│   ├── home.html          # Página principal
│   ├── core/              # Templates de conductores y lugares
│   ├── flota/             # Templates de buses
│   └── viajes/            # Templates de viajes
├── sistema_flota/         # Configuración del proyecto
│   ├── settings.py        # Configuración principal
│   ├── urls.py            # URLs principales
│   └── wsgi.py
├── manage.py
├── requirements.txt       # Dependencias del proyecto
├── README.md              # Este archivo
└── iniciar_sistema.bat    # Script de inicio para Windows
```

## Uso del Sistema

### Página Principal
- Dashboard con estadísticas generales
- Acceso rápido a todas las funciones
- Enlaces de navegación intuitivos

### Gestión de Buses
- **URL**: `/flota/buses/`
- Registro completo de información del bus
- Estados: Activo, En Mantenimiento, Inactivo
- Información técnica: placa, modelo, año, capacidad, etc.

### Gestión de Conductores
- **URL**: `/core/conductores/`
- Información personal y laboral
- Estado activo/inactivo
- Validación de datos únicos (cédula, email)

### Gestión de Lugares
- **URL**: `/core/lugares/`
- Información geográfica completa
- Soporte para coordenadas GPS
- Información de ciudad y país

### Gestión de Viajes
- **URL**: `/viajes/`
- Registro completo de viajes planificados
- Asociación de bus, conductor, origen y destino
- Estados: Programado, En Curso, Completado, Cancelado
- Captura automática de coordenadas de origen y destino
- Información de pasajeros confirmados
- Registro de fechas de salida y llegada (estimada y real)

## Características de la Interfaz

### Diseño Responsivo
- Adaptable a cualquier tamaño de pantalla
- Navegación optimizada para móviles
- Tablas con scroll horizontal en dispositivos pequeños

### Experiencia de Usuario
- Mensajes de confirmación y error
- Formularios con validación en tiempo real
- Confirmaciones antes de eliminar
- Información contextual y ayuda

### Navegación
- Sidebar persistente con navegación principal
- Breadcrumbs para ubicación actual
- Botones de acción contextuales
- Enlaces rápidos en el dashboard

## Próximas Implementaciones

### ✅ Completado
- [x] Gestión de buses
- [x] Gestión de conductores
- [x] Gestión de lugares
- [x] Gestión de viajes

### En desarrollo
- [ ] Control de costos
- [ ] Gestión de documentos de buses
- [ ] Historial de mantenimientos
- [ ] Reportes y estadísticas avanzadas

### Futuras características
- [ ] Sistema de usuarios y permisos
- [ ] Notificaciones automáticas
- [ ] Integración con APIs de mapas
- [ ] Exportación de datos
- [ ] Dashboard analítico avanzado
- [ ] Autenticación de usuarios
- [ ] Roles y permisos granulares

## Soporte y Contacto

Para soporte técnico o consultas sobre el desarrollo:
- Revisar la documentación del código
- Verificar los modelos en `models.py`
- Consultar las vistas en `views.py`
- Examinar las plantillas en `templates/`

## Licencia

Este proyecto está desarrollado para uso interno de la organización.