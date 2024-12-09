from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.serializers import ModelSerializer

from lms.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    count_of_lessons = serializers.SerializerMethodField()

    def get_count_of_lessons(self, obj):
        """Подсчет количества уроков, связанных с данным курсом"""

        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = (
            "title",
            "description",
            "preview",
            "count_of_lessons",
        )


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
