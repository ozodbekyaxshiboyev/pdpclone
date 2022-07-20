from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register((CustomUser,Course,Lesson,Task,TextTask,TextLesson))