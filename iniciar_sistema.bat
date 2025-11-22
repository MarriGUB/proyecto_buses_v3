@echo off
echo ===================================
echo  CONFIGURANDO SISTEMA DE FLOTA  
echo ===================================

echo.
echo 1. Aplicando migraciones...
python manage.py makemigrations
python manage.py migrate

echo.
echo 2. Cargando datos de ejemplo...
python manage.py cargar_datos_completos

echo.
echo 3. Creando superusuario (opcional)...
echo Para crear un superusuario, ejecute: python manage.py createsuperuser

echo.
echo 4. Iniciando servidor de desarrollo...
echo Puede acceder al sistema en: http://127.0.0.1:8000/
echo.
echo ===================================
echo     SISTEMA LISTO PARA USAR
echo ===================================
echo.
python manage.py runserver

pause