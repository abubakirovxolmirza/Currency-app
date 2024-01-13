from django.test import TestCase
from django.utils import timezone
from .models import Currency
# Create your tests here.


class CurrencyModelTest(TestCase):
    def setUp(self):
        self.currency = Currency.objects.create(
            to_money='USD',
            from_money='EUR',
            amount=100.00,
            converted_amount=120.00,
            date=timezone.now()
        )

    def test_currency_creation(self):
        self.assertIsInstance(self.currency, Currency)
        self.assertEqual(
            str(self.currency),
            "100.00 qiymatdagi pulni EURdan USDga o'girdi natija esa 120.00"
        )

    def test_currency_fields(self):
        saved_currency = Currency.objects.get(id=self.currency.id)

        self.assertEqual(saved_currency.to_money, 'USD')
        self.assertEqual(saved_currency.from_money, 'EUR')
        self.assertEqual(saved_currency.amount, 100.00)
        self.assertEqual(saved_currency.converted_amount, 120.00)
        self.assertEqual(saved_currency.date, self.currency.date)
