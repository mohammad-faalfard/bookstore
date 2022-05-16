from django.contrib.auth.models import AbstractUser
from django.db import models

'''
Create a new CustomUser model which extends AbstractUser. That means
we’re essentially making a copy where CustomUser now has inherited all
the functionality of AbstractUser, but we can override or add new
functionality as needed. We’re not making any changes yet so include the
Python pass statement which acts as a placeholder for our future code.
'''


class CustomUser(AbstractUser):
    pass


'''
The default User model in Django uses a username to uniquely identify a user during authentication.
If you'd rather use an email address, you'll need to create a custom User model 
by either subclassing AbstractUser or AbstractBaseUser .

If you have not started with a custom user model from the very first
migrate command you run, then you’re in for a world of hurt because User
is tightly interwoven with the rest of Django internally. It is challenging to
switch over to a custom user model mid-project.

AbstractUser which keeps the default User fields and
permissions or extend AbstractBaseUser which is even more granular, and
flexible, but requires more work.

There are four steps for adding a custom user model to our project:
1. Create a CustomUser model (extend AbstractUser or AbstractBaseUser)
2. Update config/settings.py (AUTH_USER_MODEL Variable)
3. Customize UserCreationForm and UserChangeForm in forms.py
4. Add the custom user model to admin.py
'''
