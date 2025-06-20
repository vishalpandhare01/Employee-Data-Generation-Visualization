from django.urls import path
from .views import (
    DepartmentListView,
    EmployeeListView,
    AttendanceListView,
    PerformanceListView,
    ProjectListView,
)

urlpatterns = [
    path('departments/', DepartmentListView.as_view()),
    path('employees/', EmployeeListView.as_view()),
    path('attendance/', AttendanceListView.as_view()),
    path('performance/', PerformanceListView.as_view()),
    path('projects/', ProjectListView.as_view()),
]

