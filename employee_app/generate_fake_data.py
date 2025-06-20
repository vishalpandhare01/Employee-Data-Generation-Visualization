import sys
import os
import django
import random
from faker import Faker
from datetime import timedelta, datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

from employee_app.models import Employee, Department, Attendance, Performance, Project

fake = Faker()

def create_departments():
    dept_names = ['HR', 'Engineering', 'Marketing', 'Finance']
    departments = []
    for name in dept_names:
        dept = Department.objects.create(name=name, location=fake.city())
        departments.append(dept)
    return departments

def create_employees(departments):
    employees = []
    for _ in range(5):
        emp = Employee.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.unique.email(),
            phone = fake.msisdn()[0:15],
            hire_date=fake.date_between(start_date='-2y', end_date='today'),
            department=random.choice(departments),
            position=fake.job(),
            salary=round(random.uniform(50000, 150000), 2)
        )
        employees.append(emp)
    return employees

def create_attendance(employees):
    for emp in employees:
        for _ in range(5):  # 5 attendance records per employee
            Attendance.objects.create(
                employee=emp,
                date=fake.date_this_month(),
                check_in=fake.time(),
                check_out=fake.time(),
                status=random.choice(['Present', 'Absent', 'Leave'])
            )

def create_performance(employees):
    for emp in employees:
        for _ in range(2):  # 2 performance reviews per employee
            Performance.objects.create(
                employee=emp,
                review_date=fake.date_between(start_date='-1y', end_date='today'),
                reviewer=fake.name(),
                rating=random.randint(1, 5),
                feedback=fake.text(max_nb_chars=200)
            )

def create_projects(employees):
    for _ in range(2):
        project = Project.objects.create(
            name=fake.bs(),
            description=fake.text(),
            start_date=fake.date_between(start_date='-1y', end_date='-1m'),
            end_date=fake.date_between(start_date='-1m', end_date='today')
        )
        project.employees.set(random.sample(employees, k=3))

if __name__ == '__main__':
    departments = create_departments()
    employees = create_employees(departments)
    create_attendance(employees)
    create_performance(employees)
    create_projects(employees)
    print("✅ Synthetic data created.")
