from django.test import TestCase
from datetime import date
from .models import Zadanie

class ZadanieModelTest(TestCase):
    def setUp(self):
        Zadanie.objects.create(opis="Testowe zadanie domowe", termin=date.today(), status="Nowe")

    def test_zadanie_tworzenie(self):
        zadanie = Zadanie.objects.get(opis="Testowe zadanie domowe")
        self.assertEqual(zadanie.status, "Nowe")
        self.assertEqual(str(zadanie), "Testowe zadanie domowe")