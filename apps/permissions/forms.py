from django.forms import ModelForm
from .models import Permission

class PermissionForm(ModelForm):
    class Meta:
        model = Permission
        fields = '__all__'