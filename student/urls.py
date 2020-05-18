from django.urls import path
from . import views

urlpatterns = [
    path("", views.hi, name='hi'),
    path("hi/<str:name>", views.say_hi_by_name),
    path("student_list", views.student_list),
    path("add_student", views.add_student),
    path("update_student/<int:id>", views.update_student),
    path("delete_student/<int:id>", views.delete_student)
]