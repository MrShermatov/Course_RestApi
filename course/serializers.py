from rest_framework import serializers
from .models import Student, Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        depth = 1

class StudentAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'image', 'name', 'address', 'number', 'course', 'grade']
        depth = 1

class StudentSerializer(serializers.ModelSerializer):
    course_write = serializers.ChoiceField(choices=Course.objects.all(), write_only=True)
    class Meta:
        model = Student
        fields = ['id', 'name', 'address', 'number', 'course', 'grade', 'course_write']
        depth = 1

    def create(self, validated_data):
        course_write = validated_data.pop('course_write')
        student = Student.objects.create(**validated_data)
        student.save()
        return student

    def update(self, instance, validated_data):
        instance.course = validated_data.pop('course_write') or instance.course
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance










