import datetime

from django.contrib.auth import get_user_model
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken as DefaultObtainAuthToken
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.api.mixins import SerializedClassesMixin
from core.models import Course, Student
from core.api.serializers import (
    StudentSerializer,
    StudentCoursesSerializer,
    CourseSerializer,
    CourseStudentsSerializer,
)
from core.api.filters import StudentFilter, CourseFilter


class StudentViewSet(SerializedClassesMixin, viewsets.ModelViewSet):
    filter_class = StudentFilter
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    serializer_classes = {"courses": StudentCoursesSerializer}

    @action(methods=("get",), detail=True)
    def courses(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)


class CourseViewSet(SerializedClassesMixin, viewsets.ModelViewSet):
    filter_class = CourseFilter
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    serializer_classes = {"students": CourseStudentsSerializer}

    @action(methods=("get",), detail=True)
    def students(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)
