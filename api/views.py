from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .serializer import CategorySerializer, ApiSerializer, CategoriaSerializer
from .models import Api, Categoria
from django.db.models import Count
from django.http import JsonResponse
from .tasks import populate_database
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def populate_apis(request):
    """
    Vista que sirve para popular la base de datos llamando a
    la task de celery 'populate_database' que creamos. Retorna un Json con el task_id si se
    ejecuto correctamente o un mensaje de error en caso contrario
    """
    if request.method == 'POST':
        result = populate_database.delay()

        return JsonResponse({'task_id': result.id}, status=200)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)


class ApiDetailView(generics.RetrieveAPIView):
    """
    Vista que devuelve los detalles (todos los campos) 
    de un objeto en particular filtrado por pk
    """
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
    lookup_field = 'pk'


class ApiListView(generics.ListAPIView):
    """
    Vista que devuelve una lista en formato JSON de todos los elementos “Api” en la 
    base de datos ordenados por defecto por pk. Recibe un parámetro opcional “order” 
    para ordenar por “Category” o “API” (admite orden inverso)
    """
    serializer_class = ApiSerializer

    def get_queryset(self):
        order_by = self.request.query_params.get('order', 'pk')
        if order_by == 'category':
            return Api.objects.order_by('Category')
        elif order_by == '-category':
            return Api.objects.order_by('-Category')
        elif order_by == 'API':
            return Api.objects.order_by('API')
        elif order_by == '-API':
            return Api.objects.order_by('-API')
        else:
            return Api.objects.all().order_by('pk')


class ApiCreateView(generics.CreateAPIView):
    """
    Crea un objeto con la estructura dada. Si no existe la categoría la crea.
    """
    serializer_class = ApiSerializer

    def create(self, request, *args, **kwargs):
        category_name = request.data.get('Category')

        category, created = Categoria.objects.get_or_create(
            nombre=category_name)

        request.data['Category'] = category.id if created else category.id

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class KeywordSearchView(generics.ListAPIView):
    """
    Esta vista devuelve en formato JSON una lista filtrada de los objetos cuyo campo “API”
    empiece con la letra que se pasa como parámetro “keyboard” (no sensible a mayúsculas o minúsculas)
    """
    serializer_class = ApiSerializer

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword', '')
        return Api.objects.filter(API__istartswith=keyword)


class CategoryListView(generics.ListAPIView):
    """
    Vista que devuelve una lista en formato JSON de las categorías creadas en la base de datos, 
    ordenados pordefecto por pk. Recibe un parámetro opcional “order” para ordenar por 
    nombre de categoría o pk (admite orden inverso). Se utiliza el Serializador 
    CategoriaSerializer que agrega el atributo count.
    """
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        order_by = self.request.query_params.get('order', 'pk')

        queryset = Categoria.objects.annotate(api_count=Count('api'))

        if order_by == '-name':
            queryset = queryset.order_by('-nombre')
        else:
            queryset = queryset.order_by('pk')

        return queryset


class CategorySearchView(generics.ListAPIView):
    """
    Devuelve una lista en formato JSON de los objetos “Api” cuya categoría concuerda con la solicitada.
    """
    serializer_class = ApiSerializer

    def get_queryset(self):
        category_name = self.request.query_params.get('category')
        return Api.objects.filter(Category__nombre__iexact=category_name)
