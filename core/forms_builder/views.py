from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import DynamicForm, FormField
from .serializers import (
    DynamicFormSerializer,
    CreateFormSerializer,
    FormFieldSerializer
)

class CreateFormView(generics.CreateAPIView):
    serializer_class = CreateFormSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class FormFieldCreateUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, form_id):
        data = request.data.copy()
        data['form'] = form_id

        serializer = FormFieldSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, field_id):
        field = FormField.objects.get(id=field_id)
        serializer = FormFieldSerializer(field, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class FormDetailView(generics.RetrieveAPIView):
    queryset = DynamicForm.objects.prefetch_related('fields')
    serializer_class = DynamicFormSerializer
    permission_classes = [IsAuthenticated]


class ReorderFieldsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, form_id):
        """
        Expected payload:
        [
            {"id": 3, "order": 1},
            {"id": 5, "order": 2}
        ]
        """
        fields = request.data

        for item in fields:
            FormField.objects.filter(
                id=item['id'],
                form_id=form_id
            ).update(order=item['order'])

        return Response({"message": "Fields reordered successfully"})


