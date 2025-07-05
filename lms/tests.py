from lms.models import Course, Lesson, Subscription
from users.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class LessonsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@sky.pro")
        self.course = Course.objects.create(
            title="Прыжки", description="В курсе представлены маленькие и большие прыжки"
        )
        self.lesson = Lesson.objects.create(
            title="Saute", description="Маленькие прыжки", owner=self.user, course=self.course,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("lms:lessons_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)

    def test_lesson_create(self):
        url = reverse("lms:lessons_create")
        data = {
            "title": "Общая физическая подготовка",
            "description": "Урок содержит упражнения для развития физической формы ученика",
            "course": self.course.pk,
            "video_url": "http://youtube.com/"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("lms:lessons_update", args=(self.lesson.pk,))
        data = {
            "title": "Прыжки. От простого к сложному",
            "description": "В курсе представлены маленькие и большие прыжки",
            "course": self.course.pk,
            "link_to_video": "http://youtube.com/",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Прыжки. От простого к сложному")

    def test_lesson_delete(self):
        url = reverse("lms:lessons_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("lms:lessons_list")
        response = self.client.get(url)
        data = response.json()
        result = {'count': 1,
                  'next': None,
                  'previous': None,
                  'results': [
                      {'id': self.lesson.pk,
                       'title': self.lesson.title,
                       'course': self.course.pk,
                       'owner': self.user.pk,
                       'video_url': self.lesson.video_url
                       }
                  ]
                  }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

class SubscriptionViewTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@sky.pro")
        self.course = Course.objects.create(
            title="Танцевальная акробатика", description="Курс включает в себя элементы партерной акробатики и полетной  акробатики", owner=self.user
        )

    def test_subscribe_to_course(self):
        """Тестирование добавления подписки на курс"""
        self.client.force_authenticate(user=self.user)
        url = reverse("lms:subscribe")
        response = self.client.post(url, {"course_id": self.course.pk})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("message"), "Подписка добавлена.")
        self.assertTrue(
            Subscription.objects.filter(user=self.user, course=self.course).exists()
        )

    def test_unsubscribe_from_course(self):
        """Тестирование удаления подписки с курса"""
        Subscription.objects.create(user=self.user, course=self.course)

        self.client.force_authenticate(user=self.user)
        url = reverse("lms:subscribe")
        response = self.client.post(url, {"course_id": self.course.pk})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("message"), "Подписка удалена.")
        self.assertFalse(
            Subscription.objects.filter(user=self.user, course=self.course).exists()
        )

    def test_subscribe_to_nonexistent_course(self):
        """Тестирование добавления подписки на несуществующий курс"""
        self.client.force_authenticate(user=self.user)
        url = reverse("lms:subscribe")
        response = self.client.post(url, {"course_id": 1000000})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_unauthenticated_user(self):
        """Тестирование доступа неаутентифицированного пользователя"""
        url = reverse("lms:subscribe")
        response = self.client.post(url, {"course_id": self.course.pk})

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)