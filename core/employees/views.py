from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Employee
from .serializers import EmployeeCreateSerializer, EmployeeListSerializer
from forms_builder.models import DynamicForm
from django.db.models import Q


class EmployeeCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EmployeeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        form = DynamicForm.objects.get(id=serializer.validated_data['form_id'])

        employee = Employee.objects.create(
            form=form,
            data=serializer.validated_data['data'],
            created_by=request.user
        )

        return Response(
            {
                "message": "Employee created successfully",
                "employee_id": employee.id
            },
            status=status.HTTP_201_CREATED
        )


class EmployeeListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Employee.objects.select_related('form')

        # 🔍 Generic search
        search = request.query_params.get('search')
        if search:
            queryset = queryset.filter(
                Q(data__icontains=search)
            )

        # 🔍 Dynamic field filtering
        for key, value in request.query_params.items():
            if key not in ['search', 'page']:
                queryset = queryset.filter(
                    data__has_key=key
                ).filter(
                    data__contains={key: value}
                )

        serializer = EmployeeListSerializer(queryset, many=True)
        return Response(serializer.data)


class EmployeeDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, employee_id):
        employee = Employee.objects.get(id=employee_id)
        employee.delete()
        return Response(
            {"message": "Employee deleted successfully"},
            status=status.HTTP_200_OK
        )


class EmployeeUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, employee_id):
        employee = Employee.objects.get(id=employee_id)

        serializer = EmployeeCreateSerializer(data={
            "form_id": employee.form.id,
            "data": request.data.get("data")
        })

        serializer.is_valid(raise_exception=True)

        employee.data = serializer.validated_data["data"]
        employee.save()

        return Response(
            {"message": "Employee updated successfully"},
            status=status.HTTP_200_OK
        )
