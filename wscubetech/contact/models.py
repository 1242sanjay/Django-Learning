from django.db import models


# Create your models here.
class Contact(models.Model):
    contact_name=models.CharField(max_length=100)
    contact_email=models.EmailField()
    contact_sub=models.CharField(max_length=100)
    contact_message=models.TextField()
    


