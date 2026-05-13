from django.urls import path

from .views import home, course_detail, student_detail, add_student, add_course, update_student

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:course_id>/', course_detail, name='course_detail'),
    path('student/<int:student_id>/', student_detail, name='student_detail'),
    path('add_student/', add_student, name='add_student'),
    path('add_course/', add_course, name='add_course'),
    path('update_student/<int:student_id>/', update_student, name='update_student'),
]