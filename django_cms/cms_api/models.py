# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    LECTURER = 'LR' 
    STUDENT = 'ST'
    role_choice = (('LECTURER', 'Lecturer'), ('STUDENT', 'Student'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=role_choice, default='LECTURER')
    faculty = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Course(models.Model):
    course_code = models.CharField(max_length=100)
    course_title = models.CharField(max_length=100)
    units = models.IntegerField()


class Lecturer(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='lecturers'
    )
    courses = models.ManyToManyField(Course,
        related_name='lecturers'
        )


class Student(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='students'
    )
    courses = models.ManyToManyField(Course,
        related_name='students'
        )
