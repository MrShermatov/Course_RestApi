from django.urls import path
from .views import CourseApiview, StudentApiView
urlpatterns =[
    path('course/', CourseApiview.as_view()),
    path('course/<int:pk>/', CourseApiview.as_view()),
    path('student/', StudentApiView.as_view()),
    path('student/<int:pk>/', StudentApiView.as_view()),

]
