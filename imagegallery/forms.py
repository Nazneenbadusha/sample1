from django import forms
from .models import ImageGallery
class  ImageForm(forms.ModelForm):
    class Meta:
        model=ImageGallery
        fields=('caption','image')
