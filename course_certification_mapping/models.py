from django.db import models
from course.models import Course
from certification.models import Certification

class CourseCertificationMapping(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE)