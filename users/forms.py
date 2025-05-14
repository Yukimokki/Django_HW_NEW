from django.contrib.auth.forms import UserCreationForm
from catalog.forms import StyleFormMixin
from users.models import CustomUser


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "password1", "password2")