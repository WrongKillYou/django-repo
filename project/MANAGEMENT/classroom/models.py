from django.db import models
from account.models import Teacher, Student


class Class(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'absent'),
        ('cutting', 'Cutting'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    time_in = models.TimeField(null=True, blank=True)
    time_out = models. TimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    written_work = models.FloatField()
    performance_task = models.FloatField()
    final_exam = models.FloatField()
    final_grade = models.FloatField()


class Merit(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    merit_name = models.CharField(max_length=255)
    merit_icon = models.TextField()
    merit_value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
