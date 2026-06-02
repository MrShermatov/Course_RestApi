from django.db import models


class Course(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-pk']

class Grade(models.Model):
    grade = models.SmallIntegerField()

    def __str__(self):
        return str(self.grade)

    class Meta:
        ordering = ['grade']

class Student(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    number = models.DecimalField(max_digits=15, decimal_places=2)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


