from django import forms
from entry_task.models import User
from entry_task.exceptions import AuthenticationFailed


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label="Username")
    password = forms.CharField(required=True,label="Password",widget=forms.PasswordInput)

    def get_username(self):
        return self['username'].value()

    def validate_credentials(self):
        username = self['username'].value()
        password = self['password'].value()
        try:
            user = User.authenticate(username, password)
            if user.role != "admin":
                raise AuthenticationFailed
            return True
        except AuthenticationFailed:
            return False