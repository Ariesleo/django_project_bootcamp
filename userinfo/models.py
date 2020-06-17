from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    uder_image = models.ImageField(upload_to='images/')