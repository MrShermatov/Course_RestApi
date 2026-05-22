
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Course, Student

class CourseApiview(APIView):
    def get(self, request: Request, pk: int=None):
        if not pk:
            courses = Course.objects.all()
            course_list = []
            for course in courses:
                course_list.append({
                    'id': course.id,
                    'name': course.name
                })
            return Response(course_list)
        else:
            course = get_object_or_404(Course, pk=pk)
            return Response(model_to_dict(course))

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


