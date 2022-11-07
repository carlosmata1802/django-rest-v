from rest_framework.viewsets import ModelViewSet
from students.models import Students
from students.api.serializers import StudentsSerializer


class StudentsViewSet(ModelViewSet):
    serializer_class = StudentsSerializer
    queryset = Students.objects.all()
