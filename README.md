# hydefx
Proyecto de terror con Cloudinary
Temática: Dr.Jekyll y Mr.Hyde...

## First Steps / Configuration...

### Python Environment
~~~bash
# antes he definido un .gitignore...
python3 -m venv .venv
source .venv/bin/activate
~~~

### Django
~~~bash
pip install django
~~~

### Project
~~~bash
django-admin startproject hydefx
# he movido los elementos generados al apartado raíz del directorio de GitHub

python manage.py runserver
~~~

## Adding SDK
- Instalar Cloudinary
~~~bash
# instalar cloudinary en el proyecto con pip
pip install cloudinary
~~~

- Configurar .env file para almacenar credenciales

- Agregar sección en settings para aplicar configuración Cloudinary / credentials a nivel global en el proyecto
~~~python
# no necesito cargar manualmente las credenciales en la instancia de Cloudinary:
cloudinary.config(
    cloud_name = '...'
)
~~~

~~~bash
# en su lugar, basta con cargar la variable de la URL de Cloudinary alojada en .env
# pip install django-environ

import environ # módulo para cargar variables de entorno (.env) == dotenv...
env = environ.Env()
environ.Env.read_env()
~~~

## Start Project
Voy a comenzar a dar forma al proyecto. Para ello, ejecutaré las migraciones a nivel interno para los modelos por defecto de Django (autenticación, administración...) y, después, empezaré a definir las distintas app que compongan toda la estructura del proyecto...

### Migraciones internas...
~~~bash
python manage.py migrate
~~~

### Primera app: lab

~~~bash
python manage.py startapp lab
# después registro la app en settings.py
~~~