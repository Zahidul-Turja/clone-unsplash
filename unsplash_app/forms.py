from django import forms

from .models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = "__all__"

        error_messages = {
            "user_name": {
                "primary_key": "Unique"
            }
        }
