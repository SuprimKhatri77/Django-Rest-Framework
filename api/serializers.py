from rest_framework import serializers
from students.models import *
from employees.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
    


