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

1. Descargar o clonar el repositorio desde GitHub.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Abrir una terminal en la carpeta donde se encuentra 'manage.py'.
4. Instalar las dependencias:

   py -m pip install -r requirements.txt

5. Aplicar las migraciones:

   py manage.py migrate

6. Importar los datos de prueba:

   py manage.py loaddata datos_prueba.json

7. Crear un superusuario:

   py manage.py createsuperuser

8. Iniciar el servidor:

   py manage.py runserver

9. Abrir la aplicación en el navegador:

   http://127.0.0.1:8000/home/

## Funcionalidades

- Página principal de la fundación.
- Catálogo dinámico de lugares patrimoniales.
- Detalle individual de cada lugar.
- Clasificación y filtrado por categorías.
- Administración mediante Django Admin.
- Inicio y cierre de sesión.
- Área de gestión restringida por permisos.
- Control de permisos para agregar y modificar lugares.
- Protección de las operaciones administrativas contra accesos no autorizados.

## Usuarios y permisos

El sistema utiliza el modelo de usuarios, grupos y permisos incorporado en Django.

**Administrador:** superusuario con acceso completo al sistema.

**Gestor Patrimonial:** usuario con 'Staff status' habilitado y perteneciente al grupo 'Gestores Patrimoniales'.

Este grupo debe tener los siguientes permisos sobre 'LugarPatrimonial':

- Can view lugar patrimonial.
- Can add lugar patrimonial.
- Can change lugar patrimonial.

El gestor puede consultar, agregar y modificar lugares patrimoniales, pero no tiene permiso para eliminarlos.

**Visitante registrado:** usuario sin permisos de gestión. Puede consultar el catálogo público, pero no acceder a la sección de gestión restringida.

### Configuración de usuarios y permisos

1. Iniciar el servidor e ingresar a http://127.0.0.1:8000/admin/ con el superusuario.
2. En Django Admin, ingresar a 'Groups'.
3. Crear un grupo llamado 'Gestores Patrimoniales'.
4. Asignarle los permisos para ver, agregar y modificar 'LugarPatrimonial'.
5. Guardar el grupo.
6. Ingresar a 'Users' y crear un usuario llamado 'gestor1'.
7. Establecer una contraseña de prueba.
8. Activar 'Staff status' para ese usuario.
9. Asociar 'gestor1' al grupo 'Gestores Patrimoniales' y guardar.
10. Crear otro usuario llamado 'visitante1'.
11. No activar 'Staff status' ni asignarle permisos administrativos a 'visitante1'.
12. Guardar los cambios.

Las contraseñas deben definirse durante la configuración y no se incluyen en el repositorio.

## Datos de prueba

El proyecto incluye el archivo 'datos_prueba.json', que contiene categorías y lugares patrimoniales para probar el funcionamiento de la aplicación.

Para cargar estos registros, ejecutar:

py manage.py loaddata datos_prueba.json

Este comando debe ejecutarse después de aplicar las migraciones.

Los datos permiten comprobar:

- El catálogo de lugares patrimoniales.
- Los detalles individuales de cada lugar.
- Los filtros por categoría.
- La visualización de imágenes e información patrimonial.

Los usuarios y grupos se configuran por separado desde Django Admin, siguiendo las instrucciones anteriores.

## Pruebas de acceso y permisos

Para comprobar el funcionamiento de las restricciones, realizar las siguientes pruebas:

**Prueba 1: Usuario sin iniciar sesión**

1. Cerrar cualquier sesión activa.
2. Intentar ingresar a http://127.0.0.1:8000/gestion/.
3. El sistema debe redirigir al formulario de inicio de sesión.

**Prueba 2: Usuario visitante1**

1. Iniciar sesión con 'visitante1'.
2. Intentar ingresar a http://127.0.0.1:8000/gestion/.
3. El sistema debe mostrar un error 403 por falta de permisos.

**Prueba 3: Usuario gestor1**

1. Iniciar sesión con 'gestor1'.
2. Ingresar a http://127.0.0.1:8000/gestion/.
3. El usuario debe poder acceder a la sección de gestión.
4. Desde Django Admin, debe poder visualizar, agregar y modificar lugares patrimoniales.
5. No debe tener permiso para eliminar lugares patrimoniales.

**Prueba 4: Administrador**

1. Iniciar sesión con el superusuario.
2. Ingresar a Django Admin.
3. Comprobar que puede administrar categorías, lugares patrimoniales, usuarios y grupos.

## Repositorio

Nombre del repositorio: CER2-ESTAYRICARDO

El repositorio público de GitHub contiene el código fuente, las dependencias, las migraciones, los datos de prueba y las instrucciones necesarias para ejecutar el proyecto.

No se incluyen contraseñas personales ni credenciales sensibles en los datos de prueba.