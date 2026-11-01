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

6. Importar los datos de prueba:

   ```bash
   py manage.py loaddata datos_prueba.json
   ```

7. Crear un superusuario:

   ```bash
   py manage.py createsuperuser
   ```

8. Iniciar el servidor:

   ```bash
   py manage.py runserver
   ```

9. Abrir la aplicación en:

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

El sistema utiliza el modelo de usuarios y permisos incorporado en Django.

**Administrador:** superusuario con acceso completo al sistema.

**Gestor Patrimonial:** usuario con `Staff status` habilitado y perteneciente al grupo `Gestores Patrimoniales`, que tiene los siguientes permisos sobre LugarPatrimonial:

- Can view lugar patrimonial.
- Can add lugar patrimonial.
- Can change lugar patrimonial.

No tiene permiso para eliminar lugares patrimoniales.

**Visitante registrado:** usuario sin permisos de gestión, que puede consultar el catálogo público, pero no acceder a la sección de gestión restringida.

### Configuración de usuarios y permisos

1. Ingresar a Django Admin con el superusuario.
2. Crear el grupo `Gestores Patrimoniales`.
3. Asignarle los permisos para ver, agregar y modificar lugares patrimoniales.
4. Crear un usuario llamado `gestor1`.
5. Activar `Staff status` para ese usuario.
6. Asociarlo al grupo `Gestores Patrimoniales`.
7. Crear opcionalmente un usuario `visitante1` sin permisos administrativos para comprobar las restricciones.

Las contraseñas deben definirse durante la configuración y no se incluyen en el repositorio.

## Datos de prueba

El proyecto incluye el archivo `datos_prueba.json`, que contiene categorías y lugares patrimoniales para probar el funcionamiento de la aplicación.

Para cargar estos registros, ejecutar:

```bash
py manage.py loaddata datos_prueba.json
```

Este comando debe ejecutarse después de aplicar las migraciones.

Los datos permiten comprobar el catálogo, los detalles individuales y los filtros por categoría.

Los usuarios y grupos se configuran por separado desde Django Admin, siguiendo las instrucciones anteriores.

## Pruebas de acceso

- Un usuario sin iniciar sesión que intenta entrar a `/gestion/` es enviado al formulario de inicio de sesión.
- Un usuario autenticado sin permisos de gestión recibe un error 403.
- Un usuario con permisos puede ingresar a Gestión y administrar lugares patrimoniales desde Django Admin.
- Un gestor sin permiso de eliminación no puede eliminar lugares patrimoniales.

## Repositorio

CER2-ESTAYRICARDO