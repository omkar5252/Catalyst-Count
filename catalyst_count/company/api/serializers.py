from rest_framework import serializers

from catalyst_count.company.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CSVUploadSerializer(serializers.Serializer):
    file = serializers.FileField(write_only=True)

    def validate_file(self, value):
        if not value.name.endswith(".csv"):
            raise serializers.ValidationError("Please upload a valid CSV file.")
        return value
