from django.urls import path
from . import views

urlpatterns = [
    path('<str:field>/startswith/<str:search_string>/', views.employee_search, name='employee_search_startswith'),
    path('<str:field>/contains/<str:search_string>/', views.employee_search, name='employee_search_contains'),
    path('<str:field>/lte/<int:search_string>/', views.employee_search, name='employee_search_lte'),
]
