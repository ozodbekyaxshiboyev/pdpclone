# Generated by Django 4.0.5 on 2022-06-22 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_customuser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='course',
            field=models.ManyToManyField(blank=True, null=True, related_name='course', to='main.course'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='course_assestant',
            field=models.ManyToManyField(blank=True, null=True, related_name='course_assestant', to='main.course'),
        ),
        migrations.AlterField(
            model_name='texttask',
            name='source_text',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
