from rest_framework.serializers import ModelSerializer
from students.models import Students


class StudentsSerializer(ModelSerializer):
    class Meta:
        model = Students
        fields = [
            "id",
            "first_name",
            "last_name",
            "date_of_birth",
            "grade",
            "phone",
            "email"
        ]
