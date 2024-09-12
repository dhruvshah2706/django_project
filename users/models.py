from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    #if user is deleted, profile is also deleted but if profile is deleted, user is not deleted
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width> 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
