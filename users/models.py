from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#inheriting from models.Model
class Profile(models.Model):
    #We want to have Profile model to have 1 to 1 relationship with the User model
    # Here CASCADE means if the user is deleted delete the profile
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    #Create a dunder str method so it displays how we want it to be displayed

    def __str__(self):
        return f'{self.user.username} Profile'
