﻿**Prueba técnica desarrollador Backend Leanware**

**-Contexto**

Projectify es una aplicación web que permite a la agencia de publicidad AdsForGood tener visibilidad sobre
el estado de sus proyectos de una manera muy simple.

**-Alcance:**

Construir un API RESTful usando Python y la tecnología de base de datos que el desarrollador guste. Que
permita a los usuarios operativos de AdsForGood reportar, cada semana, su porcentaje de dedicación a
cada uno de los proyectos de la empresa.


**Historias de Usuario:**
1. Como un usuario operativo, necesito iniciar sesión en la aplicación para obtener un JWT (JSON
Web Token) y poder disfrutar de las funcionalidades de Projectify.
2. Como un usuario operativo, quisiera poder ver todos los proyectos de la empresa.
3. Como un usuario operativo, necesito reportar por cada semana mi porcentaje de dedicación
a cada proyecto.
4. Como un usuario operativo, quisiera poder ver mis reportes pasados de dedicación.
5. Como un usuario operativo, quisiera poder editar los reportes de dedicación siempre y
cuando estén en el mismo mes calendario de la fecha de edición.

**Requerimientos no funcionales:**
1. El proyecto debe estar hecho usando Python.
2. Un usuario no debe poder reportar dos veces la misma semana-proyecto.
3. Todas las peticiones REST, exceptuando el login, deben llevar el token de autenticación en el
header Authorization: <token>.
4. Los week numbers son bajo estándar ISO (https://en.wikipedia.org/wiki/ISO_week_date).
5. El proyecto debe tener un Test Coverage > 90% con la librería de testing de tu preferencia.


**-Se desarrolla la solución usando:**

**Lenguaje:** Python 3.8.10

Framework para endpoint Api : Flask





**-Mapa de proyecto**

projectify

├── aplication.py
├── config.json
├── data_aux.py
├── data.py
├── data_test.py
├── .env
├── g_token.py
├── main.py
├── router.py
└── singleton.py



**Ruta de la aplicacion:**

```
https://projectify10.herokuapp.com/
```

**Rutas de la aplicacion**
**/login**
Metodo POST
Parametros solicitados:
name (string)-Nombre de usuario
pass(string)- Clave de acceso de usuario
Login de usuario
-Retorna Token para interactuar en las demás rutas de la  aplicación

**/new_user**
Metodo POST
Parametros solicitados:
name (string)-Nombre de usuario
pass(string)- Clave de acceso de usuario
Crear nuevo usuario
-Retorna si el usuario ha sido creado o este ya existe

**/new_project**
Metodo POST
Parametros solicitados:
start (string) - Fecha Inicio estimado del proyecto
end(string) - Fecha Inicio estimado del proyecto
name(string) - Nombre de Proyecto
Crear nuevo proyecto
-Retorna si el proyecto ha sido creado o este ya existe

**/new_report**
Metodo GET
Parametros solicitados:
porcent (string) - Porcentaje de dedicación al proyecto en la semana
week(string) - Semana a editar el porcentaje de  dedicación
name(string) - Nombre de Proyecto
Crear nuevo reporte
-Retorna Json con resultados de todos los reportes

**/reports/<user_name>**
Metodo GET
Parametros solicitados:
user_name (string) -Nombre de usuario a consultar sus reportes 
Consultar reporte por usuario
-Retorna Json con resultados de reportes por usuario

**/my_reports/**
Metodo GET
Consultar los reportes registrados por mi usuario
-Retorna Json con resultados de reportes por usuario

**/reports**
Metodo GET
Consultar todos los reportes
-Retorna Json con resultados de todos los reportes
