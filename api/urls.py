from django.urls import path
from api import views
from .views import ApiListView, ApiDetailView, ApiCreateView, KeywordSearchView, CategoryListView, CategorySearchView


urlpatterns = [

    path('items/<pk>/', ApiDetailView.as_view(), name='api-detail'),
    path('items/', ApiListView.as_view(), name='api-list'),
    path('item/create/', ApiCreateView.as_view(), name='api-create'),
    path('keyword-search/', KeywordSearchView.as_view(), name='keyword-search'),
    path('category-list/', CategoryListView.as_view(), name='category-list'),
    path('category-search/', CategorySearchView.as_view(), name='category-search'),
    path('populate-apis/', views.populate_apis, name='populate-apis'),

]
