from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import date
from .models import Zadanie

def pokaz_liste(request):
    wszystkie = Zadanie.objects.all()
    
    szukaj = request.GET.get('szukaj')
    if szukaj:
        wszystkie = wszystkie.filter(opis__icontains=szukaj)
        
    filtr = request.GET.get('filtr_status')
    if filtr:
        wszystkie = wszystkie.filter(status=filtr)

    return render(request, 'lista.html', {'zadania': wszystkie})

def zapisz_zadanie(request, pk=None):
    if pk:
        zadanie = get_object_or_404(Zadanie, pk=pk)
    else:
        zadanie = Zadanie()

    if request.method == 'POST':
        opis = request.POST.get('opis', '').strip()
        termin_str = request.POST.get('termin')
        status = request.POST.get('status')

        if not opis:
            messages.error(request, "Opis zadania nie może być pusty!")
            return render(request, 'formularz.html', {'zadanie': zadanie, 'statusy': Zadanie.STATUSY})

        if termin_str:
            wybrana_data = date.fromisoformat(termin_str)
            if wybrana_data < date.today() and not pk:
                messages.error(request, "Termin wykonania nie może być datą z przeszłości!")
                czysta_data = zadanie.termin.strftime('%Y-%m-%d') if zadanie.termin else termin_str
                return render(request, 'formularz.html', {'zadanie': zadanie, 'czysta_data': czysta_data, 'statusy': Zadanie.STATUSY})

        zadanie.opis = opis
        zadanie.termin = termin_str
        zadanie.status = status
        zadanie.save()
        return redirect('url_lista')

    czysta_data = zadanie.termin.strftime('%Y-%m-%d') if zadanie.termin else ''
    return render(request, 'formularz.html', {'zadanie': zadanie, 'czysta_data': czysta_data, 'statusy': Zadanie.STATUSY})

def usun_zadanie(request, pk):
    zadanie = get_object_or_404(Zadanie, pk=pk)
    zadanie.delete()
    return redirect('url_lista')