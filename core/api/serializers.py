from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from core.models import Student, Course


__all__ = [
    "StudentSerializer",
    "CourseSerializer",
    "StudentCoursesSerializer",
    "CourseStudentsSerializer",
]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "first_name", "last_name")


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "title", "start_date")


class StudentCoursesSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ("id", "first_name", "last_name", "courses")


class CourseStudentsSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ("id", "title", "start_date", "students")
