from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics


class StudentView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CreateStudent(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class FindStudentView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdate(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDelete(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
