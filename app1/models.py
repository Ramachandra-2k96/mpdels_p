from django.db import models

# Create your models here.
class StudentRegistration(models.Model):
    name=models.CharField(max_length=100)
    college_name=models.CharField(max_length=100)
    course_name=models.CharField(max_length=100)
    date =models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table= "app1_learning"
    def __str__(self):
        return self.name