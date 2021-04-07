from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
#User model is the sender(sends the signal)
#Create receiver function to receive the signal
#We want 1 profile to be created for each user

#sender passes the instance of the user as a part of the arguments. create_profile takes all of the arguments that the post_save() function passed to it.
#Thus, if that user was created, then create a profile object with user = instance of the user that was created.
@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    #everytime a user is created:
    if created:
        Profile.objects.create(user = instance)

#Every time the user gets saved, the profile object also gets saved.
# **kwargs accepts any other keyword argument that has been passed in addition to required arguments.
@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    #everytime a user is saved:
    instance.profile.save()
