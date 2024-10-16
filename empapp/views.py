# views.py
from django.shortcuts import render
from .models import Employee

def employee_search(request, field, lookup, search_string):
    if lookup == 'startswith':
        employees = Employee.objects.filter(**{f"{field}__startswith": search_string})
    elif lookup == 'contains':
        employees = Employee.objects.filter(**{f"{field}__contains": search_string})
    elif lookup == 'lte':
        employees = Employee.objects.filter(**{f"{field}__lte": search_string})
    else:
        employees = Employee.objects.all()
    
    return render(request, 'search_results.html', {'employees': employees})
