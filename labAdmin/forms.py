from django import forms
from django.contrib.admin.helpers import ActionForm

from .models import Sketch


class DeviceActionForm(ActionForm):
    sketch = forms.ModelChoiceField(queryset=Sketch.objects.all(), empty_label=None)
