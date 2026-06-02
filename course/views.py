
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .serializers import CourseSerializer, StudentSerializer, StudentAdminSerializer

from .models import Course, Student

class CourseApiView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer




class CourseRetrieveApiView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentApiView(ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return StudentAdminSerializer
        return StudentSerializer

    def get_queryset(self):
        grade_id = self.kwargs.get('grade')
        if grade_id:
            queryset = Student.objects.filter(grade_id=grade_id)
            return queryset

        return Student.objects.all()



class StudentRetrieveApiView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = None