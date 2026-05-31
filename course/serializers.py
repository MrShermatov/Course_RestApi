from rest_framework import serializers

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=250)
    address = serializers.CharField(max_length=250)
    number = serializers.IntegerField()
    course = serializers.IntegerField()






