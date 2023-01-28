from django.db import models

# Create your models here.
class Course(models.Model):
    course_cat = models.CharField(max_length=25)
    course_name = models.CharField(max_length=50)
    course_des = models.TextField()
    course_author = models.CharField(max_length=25)
    course_author_img = models.CharField(max_length=50)
    course_learner = models.IntegerField()
    course_like = models.IntegerField()
    course_price = models.CharField(max_length=10)
    course_img = models.CharField(max_length=50)