
1 activate venv
2 requirements.txt

admin
username vishalp
password emp@123


add fake data command
 python employee_app\generate_fake_data.py

 config 
   setting
employee_app
  serializer
  model
   url
   view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/register/', RegisterView.as_view(), name='register'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include("employee_app.urls"))
]


 urlpatterns = [
    path('departments/', DepartmentListView.as_view()),
    path('employees/', EmployeeListView.as_view()),
    path('attendance/', AttendanceListView.as_view()),
    path('performance/', PerformanceListView.as_view()),
    path('projects/', ProjectListView.as_view()),
]
