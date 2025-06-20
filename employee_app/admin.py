from django.contrib import admin
from .models import Employee , Department , Attendance , Performance , Project
# Register your models here.
emaplyee_models = [Employee , Department , Attendance , Performance , Project]
admin.site.register(emaplyee_models)