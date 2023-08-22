# django-natureforce
## 1. SIMULACRO

 El sitio es un modelo de una supuesta comunidad llamada "NatureForce". La marca no está registrada ni rige bajo ninguna norma de 
derechos de autor.

 El propósito de esta comunidad sería coleccionar fotografías de la naturaleza tomadas por distintos fotógrafos (llamados artistas),
sin embargo, no hace falta que seas el propietario de una foto para subirla. La idea es que todos los usuarios puedan subir fotos
siempre y cuando se verifique su autenticidad y se le den créditos al autor correspondiente.
 
## 2.ESTRUCTURA DEL PROYECTO

 El proyecto cuenta con tan solo una app llamada "gallery" que posee sus propias vistas, URLs y templates. Además de esta app, el proyecto
contiene una carpeta estática (static) que incluye todos los archivos que no son ni *.html* ni *.py*  y que serán utilizados.

 Por último, hay una carpeta dedicada a almacenar los archivos predeterminados y subidos por los usuarios referentes a los módelos (En
FileFields).

En cuanto a la **herencia de archivos**, el proyecto (especificamente en la app "gallery") incluye dos archivos padres:

- Padre general (parent.html) : utilizado en casi todos los archivos.
- Padre sin slider (noSliderParent) : utilizado en los formularios para evitar que el diseño se vea repetitivo.

Ambos padres incluyen un navbar y un archivo *.css* linkeado llamado "index.css"

## 3. RECORRIDO DENTRO DEL SITIO WEB

 Al iniciar el proyecto con ```python manage.py runserver``` (en consola), aparecerá una página de inicio en el localhost. Esta
página es AJENA a todas las aplicaciones presentes en el proyecto. Sin embargo, al ingresar a cualquiera de las demás secciones mediante
el uso de la barra de navegación (navbar), el sitio lo redirijirá a la aplicación "gallery".
 
Dentro de "gallery" podrá hallar una serie de vistas que se pueden acceder mediante diversos botones insertados en el sitio. Estas son:

- Inicio : página introductoria que resalta el propósito de NatureForce. Se accede mediante el botón "INICIO" presente en el navbar.
 
**URL ESTABLECIDA (/gallery/). TEMPLATE SIN TERMINAR**
 
- Galería : página que muestra todas las fotografías publicadas. Se accede mediante el botón "GALERÍA" presente en el navbar.
 
**URL ESTABLECIDA (/gallery/gallery). TEMPLATE TERMINADA**
 
- Cuenta: página que muestra los datos de la cuenta si la sesión está activa, si no, muestra la opción de registrarse e iniciar sesión.  Se
accede mediante el botón "CUENTA" presente en el navbar.
 
**URL ESTABLECIDA (/gallery/account). TEMPLATE SIN TERMINAR**

- Formulario Para Añadir Fotos: página que contiene un formulario para rellenar los datos requeridos en la clase "Photo". Cuando los datos
   son correctos, se almacena una nueva foto en la base de datos. Se accede mediante el botón "Añadir una nueva foto" en la galería.

**URL ESTABLECIDA (/gallery/addPhoto). TEMPLATE TERMINADA**

- Formulario Para Añadir Artistas: página que contiene un formulario para rellenar los datos requeridos en la clase "Artist". Cuando los
   datos son correctos, se almacena un/a nuevo/a artista en la base de datos. Se accede mediante el botón "Añadir un nuevo artista" en la
   galería.

**URL ESTABLECIDA (gallery/addArtist). TEMPLATE TERMINADA**

- Barra De Busqueda : página con la misma template de la galería, pero que muestra los datos filtrados en base a la petición del
   usuario. La barra busca entre fotos y artistas. Se acceda mediante cualquier busqueda realizada en el input presente en galería.

**URL ESTABLECIDA (gallery/search/<query>). TEMPLATE TERMINADA**

- Registro : página donde el usuario puede registrarse (crear una nueva cuenta). Se accede mediante el botón "REGISTRARSE" en
     la cuenta.

**URL ESTABLECIDA (gallery/register). TEMPLATE TERMINADA**

## 4. FORMULARIOS

En el sitio se encuentran diversos formularios, los cuáles utilizan los métodos POST y GET. Estos son:

1. AddPhotoForm :

   - **MÉTODO:** POST
   - **CAMPOS:** 4
   - **MODELO:** Photo
   - **VISTA:** addPhoto
   - **OBSERVACIÓN ESPECIAL:** Simula una llave foreana entre el campo "artista" de Photo y el campo "nombre" de Artist.

2. AddArtistForm :

   - **MÉTODO:** POST
   - **CAMPOS:** 3
   - **MODELO:** Artist
   - **VISTA:** addArtist
   - **OBSERVACIÓN ESPECIAL:** Ninguna.

3. AddUserForm :

   - **MÉTODO:** POST
   - **CAMPOS:** 3
   - **MODELO:** User
   - **VISTA:** register
   - **OBSERVACIÓN ESPECIAL:** Ninguna.

4. search :

   - **MÉTODO:** GET
   - **CAMPOS:** 1
   - **MODELO:** Artist y Photo
   - **VISTA:** search
   - **OBSERVACIÓN ESPECIAL:** Filtra las fotos que aparecen en la galería por nombre de artista y nombre de foto.


     
   

     
