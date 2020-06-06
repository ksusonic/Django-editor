from django import forms
try:
    from PIL import Image
    FIELD = forms.ImageField
except ImportError:
    FIELD = forms.FileField


class UploadForm(forms.Form):
    file = FIELD(required=True)


class AttachmentAdminForm(forms.ModelForm):
    file = FIELD(required=True)

    class Meta:
        fields = '__all__'
