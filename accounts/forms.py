from django.contrib.auth import get_user_model # import custom user model via get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
"""
the authentication system provides several built-in forms located in django.contrib.auth.forms:
UserCreationForm is A ModelForm for creating a new user.
UserChangeForm is A form used in the admin interface to change a user's information and permissions.

get_user_model
which looks to our AUTH_USER_MODEL config in settings.py. This might
feel a bit more circular than directly importing CustomUser here, but it
enforces the idea of making one single reference to the custom user model
rather than directly referring to it all over our project.
"""

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
