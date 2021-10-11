# Generated by Django 3.2.7 on 2021-10-11 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0023_question_same_course_question_text_unique'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='programmingexercise',
            constraint=models.UniqueConstraint(fields=('course', 'text'), name='same_course_programmingexercise_text_unique'),
        ),
    ]
