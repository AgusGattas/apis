# django-api-rest


## Caracteristicas

* Base de datos: Postgres
* Panel de administración (gracias a [Django](https://docs.djangoproject.com/en/3.1/intro/tutorial01/))
* Trabajos en segundo plano usando [Celery](https://docs.celeryproject.org/en/stable/)
* Utilizamos Redis
* Django Rest Framework

# Introduccion
App de django que contiene dos modelos ("Api" y "Categorias") que mediante un endpoint de metodo POST (donde una task trabajada con Celery le pega a una api externa) 
logramos cargar la base de datos de Postgres previamente estructurada gracias al ORM de Django con los modelos anteriormente descriptos. Luego una serie de 
clases asociadas a diversos endpoint nos permiten filtrar, listar y crear los distintos objetos.

# Como correr

## Ejemplificacion con Window 

Crear entorno virtual (opcional)
``` bash
virtualenv myenv
myenv\Scripts\activate
```

instale todos los requirements:
```
pip install -r requirements.txt
```

Ejecute migraciones para configurar la base de datos:
``` bash
python manage.py migrate
```

Cree un superusuario para obtener acceso al panel de administración:
``` bash
python manage.py createsuperuser
```

## Correr el proyecto:
``` bash
python manage.py runserver 
```

## Correr Redis
En una terminal inicializar a Redis que sera el broker utilizado:
``` bash
redis-server
```

## Correr Celery
Por ultimo debemos correr Celery desde una terminal para que conecte con redis y pueda gestionar las tareas:
``` bash
celery -A apisLinkChar worker -l info --concurrency 1 -P solo  
```



