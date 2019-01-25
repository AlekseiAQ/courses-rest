from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers

from core.api import views

urlpatterns = []

router = routers.DefaultRouter()
router.register(r"students", views.StudentViewSet, basename="students")
router.register(r"courses", views.CourseViewSet, basename="courses")

urlpatterns += router.urls
urlpatterns += [path("doc", get_swagger_view(title="API doc example"))]
