from django.urls import path
from .views import (
    CreateFormView,
    FormFieldCreateUpdateView,
    FormDetailView,
    ReorderFieldsView
)

urlpatterns = [
    path('forms/', CreateFormView.as_view(), name='create_form'),
    path('forms/<int:pk>/', FormDetailView.as_view(), name='form_detail'),

    path('forms/<int:form_id>/fields/', FormFieldCreateUpdateView.as_view(), name='add_field'),
    path('fields/<int:field_id>/', FormFieldCreateUpdateView.as_view(), name='update_field'),

    path('forms/<int:form_id>/reorder-fields/', ReorderFieldsView.as_view(), name='reorder_fields'),
]
