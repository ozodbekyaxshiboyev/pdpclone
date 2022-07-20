from django.urls import path,include
from .views import (AboutView,HomePageView,CourseDetail,RoleView,
MentorView,CourseCreateView,CourseLessonView,
CourseDeleteView,LessonCreateView,
LessonTaskView,LessonDeleteView,
TaskCreateView,TaskDetailView,
TaskDeleteView,TaskUpdateView,
set_assestant,noset_assestant,

user_register_view,email_activate,
registercourse,
StudentView,StudentCourseLessonView,StudentLessonTaskView,
StudentTaskDetailView,

AssistantView,AssistantStudentView,AssistantStudentLessonView,
AssistantStudentTaskView,AssistantTaskDetailView
)


urlpatterns = [
    path('', HomePageView.as_view(),name='home'),
    path('course/<int:pk>/', CourseDetail.as_view(),name='course_about'),
    path('about/', AboutView.as_view(),name='about'),

    path('role/', RoleView.as_view(),name='role'),

    path('register/<int:pk>/',registercourse,name='register'),

    path('mentor/', MentorView.as_view(),name='mentor'),
    path('mentor/coursecreate/', CourseCreateView.as_view(),name='coursecreate'),
    path('mentor/<int:pk>/courselessons/', CourseLessonView.as_view(),name='lessons'),
    path('mentor/<int:pk>/courselessons/set/', set_assestant,name='set'),
    path('mentor/<int:pk>/courselessons/noset/<int:u_pk>/', noset_assestant,name='noset'),
    path('mentor/<int:pk>/coursedelete/', CourseDeleteView.as_view(),name='coursedelete'),
    path('mentor/<int:pk>/lessoncreate/', LessonCreateView.as_view(),name='lessoncreate'),
    path('mentor/<int:pk>/<int:lesson_pk>/', LessonTaskView.as_view(),name='tasks'),
    path('mentor/<int:pk>/<int:lesson_pk>/lessondelete/', LessonDeleteView.as_view(),name='lessondelete'),
    path('mentor/<int:pk>/<int:lesson_pk>/taskcreate/', TaskCreateView.as_view(),name='taskcreate'),
    path('mentor/<int:pk>/<int:lesson_pk>/<int:task_pk>/', TaskDetailView.as_view(),name='taskdetail'),
    path('mentor/<int:pk>/<int:lesson_pk>/<int:task_pk>/delete', TaskDeleteView.as_view(),name='taskdelete'),
    path('mentor/<int:pk>/<int:lesson_pk>/<int:task_pk>/update', TaskUpdateView.as_view(),name='taskupdate'),


    # path('login/', login_view, name='login'),
    path('activate-email/', email_activate, name='activate-email'),
    path('signup/', user_register_view, name='signup'),

    path('student/',StudentView.as_view(),name='student'),
    path('student/<int:pk>/courselessons/', StudentCourseLessonView.as_view(),name='studentlessons'),
    path('student/<int:pk>/<int:lesson_pk>/', StudentLessonTaskView.as_view(),name='studenttasks'),
    path('student/<int:pk>/<int:lesson_pk>/<int:task_pk>/', StudentTaskDetailView.as_view(),name='studenttaskdetail'),

    path('assistant/',AssistantView.as_view(),name='assistant'),
    path('assistant/<int:pk>/students/',AssistantStudentView.as_view(),name='assistantstudent'),
    path('assistant/<int:pk>/<int:student_pk>/',AssistantStudentLessonView.as_view(),name='assistantstudentlesson'),
    path('assistant/<int:pk>/<int:student_pk>/<int:lesson_pk>/',AssistantStudentTaskView.as_view(),name='assistantstudenttask'),
    path('assistant/<int:pk>/<int:student_pk>/<int:lesson_pk>/<int:task_pk>/',AssistantTaskDetailView.as_view(),name='assistanttaskdetail'),

]
