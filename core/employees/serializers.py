from rest_framework import serializers
from .models import Employee
from forms_builder.models import FormField
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from datetime import datetime


class EmployeeCreateSerializer(serializers.Serializer):
    form_id = serializers.IntegerField()
    data = serializers.JSONField()

    def validate(self, attrs):
        form_id = attrs['form_id']
        data = attrs['data']

        fields = FormField.objects.filter(form_id=form_id)

        field_map = {field.label: field for field in fields}

        # 1. Check required fields
        for field in fields:
            if field.required and field.label not in data:
                raise serializers.ValidationError(
                    f"Missing required field: {field.label}"
                )

        # 2. Check unknown fields
        for key in data.keys():
            if key not in field_map:
                raise serializers.ValidationError(
                    f"Unknown field: {key}"
                )

        # 3. Validate field types
        for label, value in data.items():
            field = field_map[label]
            field_type = field.field_type

            try:
                if field_type == 'number':
                    float(value)

                elif field_type == 'date':
                    datetime.strptime(value, '%Y-%m-%d')

                elif field_type == 'email':
                    validate_email(value)

                elif field_type in ['text', 'textarea', 'password']:
                    if not isinstance(value, str):
                        raise ValueError

            except Exception:
                raise serializers.ValidationError(
                    f"Invalid value for field '{label}'"
                )

        return attrs


class EmployeeListSerializer(serializers.ModelSerializer):
    form_name = serializers.CharField(source='form.name', read_only=True)

    class Meta:
        model = Employee
        fields = (
            'id',
            'form',
            'form_name',
            'data',
            'created_at',
        )
