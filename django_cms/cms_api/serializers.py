from rest_framework import 
from django.contrib.auth.models import User

from .models import Profile, Course, Lecturer, Student

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'firstname', 'lastname','username')


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ('id', 'user_id', 'role','faculty', 'department')


class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ('id', 'course_code', 'course_title','units')


class LecturerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lectuer
        fields = ('id', 'user_id', 'courses')


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ('id', 'user_id', 'courses')

