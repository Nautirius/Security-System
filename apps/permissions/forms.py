from django.forms import ModelForm, Form, ModelMultipleChoiceField, CharField
from .models import Permission


class PermissionForm(ModelForm):
    def __init__(self, *args, title, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["label"].widget.attrs.update({"class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-slate-500 focus:ring-slate-500 sm:text-sm"})
        self.fields["zones"].widget.attrs.update({"class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-slate-500 focus:ring-slate-500 sm:text-sm"})
        self.fields["users"].widget.attrs.update({"class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-slate-500 focus:ring-slate-500 sm:text-sm"})
        self.title = title

    class Meta:
        model = Permission
        fields = '__all__'


class UserPermissionForm(Form):
    user = CharField(label="User", initial=None, disabled=True)
    permissions = ModelMultipleChoiceField(label="Permissions", queryset=Permission.objects.all())

    def __init__(self, *args, user, title, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].widget.attrs.update({"class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-slate-500 focus:ring-slate-500 sm:text-sm"})
        self.fields["permissions"].widget.attrs.update({"class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-slate-500 focus:ring-slate-500 sm:text-sm"})
        self.title = title
        self.fields["user"].initial = f"{user}"
        self.fields["permissions"].initial = user.permission_set.all()


class ZonePermissionForm(Form):
    zone = CharField(label="Zone", initial=None, disabled=True)
    permissions = ModelMultipleChoiceField(label="Permissions", queryset=Permission.objects.all())

    def __init__(self, *args, zone, title, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["zone"].widget.attrs.update({"class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm "
                                                          "focus:border-slate-500 focus:ring-slate-500 sm:text-sm"})
        self.fields["permissions"].widget.attrs.update({"class": "mt-1 block w-full rounded-md border-gray-300 "
                                                                 "shadow-sm focus:border-slate-500 "
                                                                 "focus:ring-slate-500 sm:text-sm"})
        self.title = title
        self.fields["zone"].initial = f"{zone}"
        self.fields["permissions"].initial = zone.permission_set.all()
