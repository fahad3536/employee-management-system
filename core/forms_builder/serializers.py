from rest_framework import serializers
from .models import DynamicForm, FormField


class FormFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormField
        fields = (
            'id',
            'label',
            'field_type',
            'required',
            'order',
            'form'
        )


class DynamicFormSerializer(serializers.ModelSerializer):
    fields = FormFieldSerializer(many=True, read_only=True)

    class Meta:
        model = DynamicForm
        fields = (
            'id',
            'name',
            'description',
            'fields',
        )


class CreateFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicForm
        fields = ('id', 'name', 'description')
