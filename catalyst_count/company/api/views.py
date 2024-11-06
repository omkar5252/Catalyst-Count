from rest_framework import viewsets

from catalyst_count.company.api.filters import CompanyFilter
from catalyst_count.company.models import Company
from catalyst_count.company.tasks import process_csv
from .serializers import CSVUploadSerializer, CompanySerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

class CompanyViewSet(viewsets.GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filterset_class = CompanyFilter

    def get_serializer_class(self):
        # Return different serializers based on the action
        if self.action == "upload_csv":
            return CSVUploadSerializer
        return CompanySerializer

    @action(detail=False, methods=['post'], url_path='upload-csv')
    def upload_csv(self, request, *args, **kwargs):
        # Validate and parse the file using the serializer
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            csv_file = serializer.validated_data['file']
            # Save the file temporarily
            fs = FileSystemStorage()
            filename = fs.save(csv_file.name, csv_file)
            file_path = fs.path(filename)

            # Process the CSV file asynchronously using Celery
            process_csv.delay(file_path)

            return Response(
                {"message": "File uploaded successfully. Processing started."},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
