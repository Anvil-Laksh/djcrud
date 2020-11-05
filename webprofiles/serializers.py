from rest_framework import serializers

from webprofiles.models import EmployeeProfiles


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfiles
        fields = "__all__"
