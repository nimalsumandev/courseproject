from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=50)
    duration = models.CharField(max_length=100)
    fee = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name
