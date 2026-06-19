from django.db import models

class Zadanie(models.Model):
    STATUSY = [
        ('Nowe', 'Nowe'),
        ('W trakcie', 'W trakcie'),
        ('Zakończone', 'Zakończone'),
    ]

    opis = models.CharField(max_length=255)
    termin = models.DateField()
    status = models.CharField(max_length=20, choices=STATUSY, default='Nowe')

    def __str__(self):
        return self.opis