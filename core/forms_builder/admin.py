from django.contrib import admin
from .models import DynamicForm, FormField


class FormFieldInline(admin.TabularInline):
    model = FormField
    extra = 1


@admin.register(DynamicForm)
class DynamicFormAdmin(admin.ModelAdmin):
    inlines = [FormFieldInline]
    list_display = ('id', 'name', 'created_by', 'created_at')


@admin.register(FormField)
class FormFieldAdmin(admin.ModelAdmin):
    list_display = ('label', 'field_type', 'form', 'order')
