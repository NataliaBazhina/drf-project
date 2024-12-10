from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Payment
from .serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    filterset_fields = ('paid_course','paid_lesson','type',)




    #filter_backends = (DjangoFilterBackend, OrderingFilter)
    #filterset_class = PaymentFilter  # Убедитесь, что вы создали фильтры для модели Payment
    #ordering_fields = ['payment_date', 'amount']  # Поля, по которым можно сортировать
    #ordering = ['payment_date']