from django import forms
from .models import Details




class ChangeProfilePic(forms.ModelForm):
    class Meta:
        model = Details
        fields =['profilePic']



