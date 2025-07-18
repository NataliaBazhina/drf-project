from celery import shared_task
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import smtplib
import logging

logger = logging.getLogger(__name__)


@shared_task(bind=True, max_retries=3)
def subscription_message(self, course, email):
    try:
        send_mail(
            subject="Сообщение о подписке",
            message=f"Материалы курса {course} обновились",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False
        )
        logger.info(f"Письмо для {email} успешно отправлено")

    except smtplib.SMTPAuthenticationError as e:
        error_msg = f"Ошибка аутентификации SMTP: {str(e)}"
        logger.error(error_msg)
        print(f"❌ {error_msg}")
        raise self.retry(exc=e, countdown=60)  # Повтор через 60 секунд

    except smtplib.SMTPException as e:
        error_msg = f"Ошибка SMTP при отправке на {email}: {str(e)}"
        logger.error(error_msg)
        print(f"⚠️ {error_msg}")
        raise self.retry(exc=e, countdown=120)

    except Exception as e:
        error_msg = f"Неожиданная ошибка для {email}: {str(e)}"
        logger.exception(error_msg)  # Логирует traceback
        print(f"🔥 {error_msg}")
        raise self.retry(exc=e, countdown=300)