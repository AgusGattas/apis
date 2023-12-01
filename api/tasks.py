from celery import shared_task
import requests
from .models import Api, Categoria
from celery import Celery


@shared_task
def populate_database():
    """
    Tarea creada para la carga de datos a la DB utilizando la informacion de la api externa
    https://api.publicapis.org/entries, primero cargando la tabla Categoria y luego la tabla
    Api para respetar la integracion de datos.

    Retorna un mensaje de aprobacion o de error segun sea el resultado 

    """
    try:
        response = requests.get('https://api.publicapis.org/entries')
        data = response.json()

        entries = data.get('entries', [])
        print(len(entries))
        for ent in entries:
            category_name = ent.get('Category', 'Default Category')

            # Buscar o crear la categoría
            category, created = Categoria.objects.get_or_create(
                nombre=category_name)

            # Crear la API asociada a la categoría
            Api.objects.create(
                API=ent.get('API'),
                Description=ent.get('Description'),
                Auth=ent.get('Auth'),
                HTTPS=ent.get('HTTPS'),
                Cors=bool(ent.get('Cors', '').lower() == "yes"),
                Link=ent.get('Link'),
                Category=category
            )

        return {'message': 'Datos guardados exitosamente en la base de datos'}
    except requests.RequestException as e:
        # Agrega esta línea para imprimir el error
        print(f'Error en la solicitud: {e}')
        return {'error': str(e)}
