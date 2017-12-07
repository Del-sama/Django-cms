# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    role_choice = (('Lecturer', 'Lecturer'), ('Student', 'Student'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=role_choice, default='Lecturer')
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
        related_name='lecturer'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lecturer'
    )


class Student(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='student'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='student'
    )
    