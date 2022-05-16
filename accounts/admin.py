from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)


"""
We'll extend the existing UserAdmin into CustomUserAdmin and tell Django
to use our new forms, custom user model, and list only the email and
username of a user. If we wanted to we could add more of the existing User
fields to list_display such as is_staff.

A good way to confirm our custom user model is up and running properly is
to create a superuser account so we can log into the admin. This command
will access CustomUserCreationForm under the hood.

$ docker-compose exec web python manage.py createsuperuser
"""