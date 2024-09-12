from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs): 
    if created:
        Profile.objects.create(user = instance)
# once the user is created, a signal of post_save is sent by the User(sender) and is received by the receiver
# which executes the function. instance = instance of the user, created = if user was created

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs): 
    instance.profile.save()