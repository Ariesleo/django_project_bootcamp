from django.db import models

# Create your models here.

class ArticleInfo(models.Model):
    user_image = models.ImageField(upload_to='images/')
    article_topic = models.CharField(max_length=30)
    pub_date = models.DateField()
    article_demo_image = models.ImageField(upload_to='images/')
    article_link = models.CharField(max_length=250)
    art_cont_display = models.CharField(max_length=300)
