from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.name



class CustomUser(models.Model):
    phone_number = models.CharField(max_length=13)
    profile_image=models.ImageField(upload_to='user_images',null=True,blank=True)
    verify_code = models.CharField(max_length=100,null=True,blank=True)
    course = models.ManyToManyField('Course',related_name='course',null=True,blank=True)
    course_assestant = models.ManyToManyField('Course',related_name='course_assestant',null=True,blank=True)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.user)



class Lesson(models.Model):
    course = models.ForeignKey('Course',on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=100)
    source_file = models.FileField(upload_to='lesson_files',null=True,blank=True)
    video_file = models.FileField(upload_to='lesson_videos',null=True,blank=True)
    others = models.CharField(max_length=512,null=True,blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    number = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='task_images',null=True,blank=True)
    lesson = models.ForeignKey('Lesson',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)



class TextTask(models.Model):
    user = models.ForeignKey('CustomUser',on_delete=models.CASCADE)
    task = models.ForeignKey('Task',on_delete=models.CASCADE)
    is_user = models.BooleanField(default=False)
    source_file = models.FileField(upload_to='texttask_files', null=True, blank=True)
    source_text = models.CharField(max_length=512, null=True, blank=True)
    send_time = models.DateTimeField(auto_now_add=True)



class TextLesson(models.Model):
    user = models.ForeignKey('CustomUser',on_delete=models.CASCADE)
    lesson = models.ForeignKey('Lesson',on_delete=models.CASCADE)
    is_user = models.BooleanField(default=False)
    source_file = models.FileField(upload_to='textlesson_files', null=True, blank=True)
    source_text = models.CharField(max_length=512)
    send_time = models.DateTimeField(auto_now_add=True)





