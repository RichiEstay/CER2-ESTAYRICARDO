# Certamen 2 - Fundación Patrimonio Vivo

**Estudiante:** Ricardo Estay  
**Asignatura:** Taller Lenguaje de Programación  
**Carrera:** Ingeniería en Informática

## Descripción del proyecto

Aplicación web desarrollada con Python y Django Framework para la Fundación Patrimonio Vivo.

El sistema permite consultar un catálogo de lugares patrimoniales de Chile, visualizar sus detalles y filtrar los registros por categoría.

Además, incorpora un sistema de inicio y cierre de sesión, una sección de gestión restringida y permisos para administrar lugares patrimoniales.

## Tecnologías utilizadas

- Python
- Django Framework
- SQLite
- HTML
- Bootstrap
- Django Template Language (DTL)

## Instalación y ejecución

1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Abrir una terminal en la carpeta donde se encuentra `manage.py`.
4. Instalar las dependencias:

   ```bash
   py -m pip install -r requirements.txt
   ```

5. Aplicar las migraciones:

   ```bash
   py manage.py migrate
   ```

6. Crear un superusuario:

   ```bash
   py manage.py createsuperuser
   ```

7. Iniciar el servidor:

   ```bash
   py manage.py runserver
   ```

8. Abrir la aplicación en:

   http://127.0.0.1:8000/home/

## Funcionalidades

- Página principal de la fundación.
- Catálogo dinámico de lugares patrimoniales.
- Detalle individual de cada lugar.
- Clasificación y filtrado por categorías.
- Administración mediante Django Admin.
- Inicio y cierre de sesión.
- Área de gestión para usuarios autenticados y autorizados.
- Control de permisos para agregar y modificar lugares.

## Usuarios y permisos

El sistema utiliza el modelo de usuarios y permisos incorporado en Django.

**Administrador:** superusuario con acceso completo al sistema.

**Gestor Patrimonial:** usuario con `Staff status` habilitado y perteneciente al grupo `Gestores Patrimoniales`, que tiene los siguientes permisos sobre LugarPatrimonial:

- Can view lugar patrimonial.
- Can add lugar patrimonial.
- Can change lugar patrimonial.

**Visitante registrado:** usuario sin permisos de gestión, que puede consultar el catálogo público, pero no acceder a la sección de gestión restringida.

Para configurar los permisos, ingresar a Django Admin con un superusuario, crear el grupo `Gestores Patrimoniales`, asignarle los permisos indicados y asociar los usuarios correspondientes.

## Datos de prueba

Después de crear el superusuario, ingresar a Django Admin para registrar categorías y lugares patrimoniales.

Se pueden utilizar las categorías Monumentos y Edificios históricos, junto con lugares como Palacio Baburizza, Palacio Rioja y Moáis de Rapa Nui.

Los usuarios de prueba pueden crearse desde Django Admin, sin utilizar contraseñas reales o personales.

## Repositorio

CER2-ESTAYRICARDO