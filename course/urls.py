from django.urls import path
from .views import (CourseApiView, StudentApiView,
                    CourseRetrieveApiView, StudentRetrieveApiView,
                    )
urlpatterns =[
    path('course/', CourseApiView.as_view()),
    path('course/<int:pk>/', CourseRetrieveApiView.as_view()),

    path('student/', StudentApiView.as_view()),
    path('student/<int:pk>/', StudentRetrieveApiView.as_view()),
    path('student/grade/<int:grade>/', StudentApiView.as_view()),

]
