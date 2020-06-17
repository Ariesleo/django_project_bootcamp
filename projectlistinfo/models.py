from django.db import models

# Create your models here.
class ProjectListInfo(models.Model):
    user_email = models.EmailField()
    project_name = models.CharField(max_length=50)
    proj_demo_link = models.CharField(max_length=250)
    proj_source_link = models.CharField(max_length=250)
    tools_used = models.CharField(max_length=250)
    remarks = models.TextField()
    pub_date = models.DateTimeField()