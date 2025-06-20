```markdown
# Django REST API Setup

This project is a Django REST Framework application for managing employees, departments, attendance, performance, and projects.

---

## Project Structure

```

config/
└── settings.py
manage.py
employee\_app/
├── serializer/
├── model/
├── url.py
└── view\.py
venv/
.env
requirements.txt
README.md

````

---

## Setup Instructions

### 1. Activate Virtual Environment

- On Windows:
  ```bash
  venv\Scripts\activate
````

* On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Admin Credentials

* **Username:** vishalp
* **Password:** emp\@123

---

## Running the Server

Start the Django development server:

```bash
python manage.py runserver
```

---

## Add Fake Data

To populate the database with fake data, run:

```bash
python employee_app\generate_fake_data.py
```

---

## API Endpoints

All API endpoints are prefixed with `http://127.0.0.1:8000/api/v1/`

| Endpoint          | Description         |
| ----------------- | ------------------- |
| `/register/`      | User registration   |
| `/token/`         | Obtain JWT token    |
| `/token/refresh/` | Refresh JWT token   |
| `/departments/`   | List of departments |
| `/employees/`     | List of employees   |
| `/attendance/`    | Attendance records  |
| `/performance/`   | Performance data    |
| `/projects/`      | Projects list       |

### Example:

* To get the list of employees, visit:
  `http://127.0.0.1:8000/api/v1/employees/`

---

## URL Patterns

### Main URLs (`config/urls.py`)

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/register/', RegisterView.as_view(), name='register'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include("employee_app.urls")),
]
```

### Employee App URLs (`employee_app/urls.py`)

```python
urlpatterns = [
    path('departments/', DepartmentListView.as_view()),
    path('employees/', EmployeeListView.as_view()),
    path('attendance/', AttendanceListView.as_view()),
    path('performance/', PerformanceListView.as_view()),
    path('projects/', ProjectListView.as_view()),
]
```

---

## Notes

* Ensure `.env` file contains your environment variables.
* Use Django admin panel at `http://127.0.0.1:8000/admin/` to manage data through UI.
* Make sure virtual environment is activated before running any management commands.
