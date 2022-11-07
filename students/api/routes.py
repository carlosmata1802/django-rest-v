from rest_framework.routers import DefaultRouter
from students.api.views import StudentsViewSet


router_students = DefaultRouter()
router_students.register(r"students", StudentsViewSet)
