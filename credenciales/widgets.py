from django.forms.widgets import ClearableFileInput
from django.utils.html import format_html

class CustomClearableFileInput(ClearableFileInput):
    template_name = 'widgets/custom_clearable_file_input.html'

