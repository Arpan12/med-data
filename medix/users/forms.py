from django import forms
from django.contrib.auth import get_user_model

from crispy_forms.bootstrap import FormActions, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit

from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = forms.ALL_FIELDS

class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username','name','email','mobile']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                Div(
                    Field('username', placeholder='Username'), 
                    css_class = 'col-md-6'
                    ),
                Div(
                    PrependedText('mobile', '+91', placeholder='Mobile Number'),
                    css_class = 'col-md-6'
                    ),
                Div(
                    Field('name', placeholder='Name'), 
                    css_class = 'col-md-12'
                    ),
                Div('email', css_class = 'col-md-12'),
                Div('password1', css_class = 'col-md-6'),
                Div('password2', css_class = 'col-md-6')
                ),
            FormActions(
                Submit('submit', 'Sign Up', css_class='btn btn-success btn-block')
                )
            )
        self.helper.form_id = 'signup_form'
        self.helper.form_class = 'sign'
        self.helper.form_method = 'post'
        self.helper.form_action = 'account_signup'
        self.helper.form_show_labels = False
        super(SignupForm, self).__init__(*args, **kwargs)


    def signup(self, request, user):
        user.username = self.cleaned_data['username']
        user.name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        user.mobile = self.cleaned_data['mobile']
        user.is_superuser = False
        user.is_active = True
        user.save()
