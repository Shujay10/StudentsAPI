from django.urls import path
from . import views

urlpatterns = [
    path('viewStudents', views.StudentView.as_view()),
    path('createStudent', views.CreateStudent.as_view()),
    path('findStudents/<int:pk>', views.FindStudentView.as_view()),
    path('updateStudents/<int:pk>', views.StudentUpdate.as_view()),
    path('deleteStudents/<int:pk>', views.StudentDelete.as_view()),
]
