from django.db import models
from django.contrib.auth import get_user_model
from forms_builder.models import DynamicForm

User = get_user_model()


class Employee(models.Model):
    form = models.ForeignKey(
        DynamicForm,
        on_delete=models.PROTECT,
        related_name='employees'
    )
    data = models.JSONField()  # dynamic form values
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='employees'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Employee {self.id} - Form: {self.form.name}"
