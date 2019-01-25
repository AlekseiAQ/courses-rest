from django_filters import rest_framework as filters

from core.models import Student, Course


class StudentFilter(filters.FilterSet):
    class Meta:
        model = Student
        fields = "__all__"


class CourseFilter(filters.FilterSet):
    class Meta:
        model = Course
        fields = "__all__"
