from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Course(models.Model):
    title = models.CharField(max_length=150)

    start_date = models.DateField()

    students = models.ManyToManyField(Student, related_name="courses", blank=True)

    def __str__(self):
        return self.title
