
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from unicodedata import category

from .serializers import CourseSerializer, StudentSerializer

from .models import Course, Student

class CourseApiview(APIView):
    def get(self, request: Request, pk: int=None):
        if not pk:
            courses = Course.objects.all()

            return Response(CourseSerializer(courses, many=True).data)
        else:
            course = get_object_or_404(Course, pk=pk)
            return Response(CourseSerializer(course).data)

    def post(self, request: Request, pk: int=None):
        if pk:
            return Response({'message': 'Method Not Post Allowed'}, status=405)
        serializer= CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        course = Course.objects.create(
            **serializer.validated_data.get,
        )
        return Response(CourseSerializer(course).data)

    def put(self, request: Request, pk: int=None):
        if pk:
            course =get_object_or_404(Course, pk=pk)
            serializer = CourseSerializer(instance=course, data=request.data)
            serializer.is_valid(raise_exception=True)

            course.name = serializer.validated_data.get('name', course.name)

            course.save()
            return Response(CourseSerializer(course).data)
        else:
            return Response({'message': 'Method Not Post Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request: Request, pk: int=None):
        if  not pk:
            return Response({'message': 'Method Not Post Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        if pk:
            course = get_object_or_404(Course, pk=pk)
            course.delete()
            return Response({'message': "Course delete succesfull"}, status=status.HTTP_204_NO_CONTENT)

class StudentApiView(APIView):
    def get(self, request: Request, pk:int=None):
        if not pk:
            students = Student.objects.all()
            students_list = []
            for student in students:
                students_list.append(
                    {
                        'id': student.id,
                        'name': student.name,
                        'number': student.number,
                        'address': student.address
                    }
                )
            return Response(students_list)
        else:
            student  = get_object_or_404(Student, pk=pk)
            return Response(model_to_dict(student))

    def post(self, request: Request, pk: int = None):
        if pk:
            return Response({'message': 'Method Not Post Allowed'}, status=405)
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = Course.objects.create(
            **serializer.validated_data.get,
        )
        return Response(StudentSerializer(student).data)

    def put(self, request: Request, pk: int = None):
        if pk:
            student = get_object_or_404(Student, pk=pk)
            serializer = StudentSerializer(instance=student, data=request.data)
            serializer.is_valid(raise_exception=True)

            student.name = serializer.validated_data.get('name', student.name)
            student.number = serializer.validated_data.get('number', student.number)
            student.address = serializer.validated_data.get('address', student.address)
            student.course_id = serializer.validated_data.get('student', student.course_id)

            student.save()
            return Response(StudentSerializer(student).data)
        else:
            return Response({'message': 'Method Not Post Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request: Request, pk: int = None):
        if not pk:
            return Response({'message': 'Method Not Post Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        if pk:
            student = get_object_or_404(Student, pk=pk)
            student.delete()
            return Response({'message': "Student delete succesfull"})


