from django.db import models

# OnlineCourses
# add course
class add_courses(models.Model):
    Course_name=models.CharField(max_length=50,unique='true')
    Details=models.CharField(max_length=100)
    Fees=models.IntegerField()
    Duration=models.CharField(max_length=50)
    Image=models.CharField(max_length=50)
    Mode=models.CharField(max_length=10)

    

