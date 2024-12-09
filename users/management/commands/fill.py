from django.core.management.base import BaseCommand
from users.models import Payment, User


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Create user and payments"""

        params = dict(username='test', email='test@example.com', password='qwerty')
        user, user_status = User.objects.get_or_create(**params)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print('User created successfully.')

        Payment.objects.create(
            owner=user1,
            payment_date='2023-10-01',
            paid_course_id=1,
            paid_lesson=None,
            amount=100.00,
            type='CASH'
        )

        Payment.objects.create(
            owner=user2,
            payment_date='2023-10-02',
            paid_course=None,
            paid_lesson_id=2,
            amount=150.00,
            type='BANK_TRANSFER'
        )

        self.stdout.write(self.style.SUCCESS('Данные о платежах успешно загружены!'))