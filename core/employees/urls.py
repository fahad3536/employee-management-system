from django.urls import path
from .views import (
    EmployeeCreateView,
    EmployeeListView,
    EmployeeDeleteView,
    EmployeeUpdateView
)

urlpatterns = [
    path('employees/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/list/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/<int:employee_id>/', EmployeeDeleteView.as_view(), name='employee_delete'),
    path('employees/<int:employee_id>/update/', EmployeeUpdateView.as_view()),
]
