from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    registration = serializers.IntegerField(source='regno')
    gradeAfterAYear = serializers.SerializerMethodField(method_name='cal_class')

    class Meta:
        model = Student
        fields = ['id', 'name', 'grade', 'registration', 'gradeAfterAYear']

    def cal_class(self, product: Student):
        return product.grade + 1
