from rest_framework import serializers
from .models import Course, Lesson
from .validators import validate_links

class LessonSerializer(serializers.ModelSerializer):
    video_url = serializers.CharField(validators=[validate_links])

    class Meta:
        model = Lesson
        fields = ["id","title", "course","owner","video_url"]


class CourseSerializer(serializers.ModelSerializer):
    count_of_lessons = serializers.SerializerMethodField()
    info_lessons = serializers.SerializerMethodField()

    def get_count_of_lessons(self, obj):
        return obj.lesson_set.count()

    def get_info_lessons(self, obj):
        lessons = obj.lesson_set.all()
        return LessonSerializer(lessons, many=True).data

    class Meta:
        model = Course
        fields = (
            "title",
            "description",
            "preview",
            "count_of_lessons",
            "info_lessons",
        )
