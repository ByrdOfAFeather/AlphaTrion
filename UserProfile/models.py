from django.contrib.auth.models import User
from django.db import models

GRADE_LEVELS = [
	(9, 9),
	(10, 10),
	(11, 11),
	(12, 12)
]

class Student(models.Model):
	user = models.OneToOneField(User, null=True)
	grade_level = models.PositiveIntegerField(choices=GRADE_LEVELS, default=3)