from django import template
from django.apps import apps
from django.core.exceptions import FieldDoesNotExist
register = template.Library()

variable_rename = {
    'assigned_section': 'Routed',
    'contact_first_name': 'Contact first name',
    'contact_last_name': 'Contact last name',
    'location_city_town': 'City',
    'location_name': 'Location name',
    'location_state': 'State',
    'assigned_to': 'Assignee',
    'public_id': 'Complaint ID',
    'primary_statute': 'Classification',
    'violation_summary': 'Personal description',
}


@register.filter(name='get_field_label')
def get_field_label(value, arg):
    """
    Return label for given model/field from cts_forms app
    If no field exists, we expect it's a filter field like
    `create_date_end',  strip underscores for display
    """
    try:
        model = apps.get_model('cts_forms', value)
        field = model._meta.get_field(arg)
    except FieldDoesNotExist:
        return arg.replace('_', ' ')

    return variable_rename.get(field.name, field.verbose_name)
