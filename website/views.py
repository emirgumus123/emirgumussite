from django.shortcuts import render
from .models import Slider , Haberler , Hizmetler
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings
from .forms import ContactForm



# Create your views here.

def anasayfa(request):
    sliders = Slider.objects.all().order_by('order')
    haberler = Haberler.objects.all().order_by('-created_at')[:4]  # Son 4 haberi al
    context = {
        'sliders': sliders,
        'haberler': haberler,
    }
    return render(request, 'anasayfa.html' , context)

def haber_detay(request, haber_id):
    haber = get_object_or_404(Haberler, id=haber_id)
    context = {
        'haber': haber,
    }
    return render(request, 'haber_detay.html', context)

def hakkimizda(request):
    return render(request, 'hakkimizda.html')

def haber_listesi(request):
    haberler = Haberler.objects.all().order_by('-created_at')  # Tüm haberleri al ve en son eklenenler en üstte görünsün
    return render(request, 'haberler.html', {'haberler': haberler})

def hizmetler(request):
    hizmetler = Hizmetler.objects.all().order_by('order')  # Hizmetleri sıralı olarak al
    context = {
        'hizmetler': hizmetler,
    }
    return render(request, 'hizmetler.html' , context)

def hizmet_detay(request, pk):
    hizmet = get_object_or_404(Hizmetler, id=pk)
    context = {
        'hizmet': hizmet,
    }
    return render(request, 'hizmet_detay.html', context)


def iletisim(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız başarıyla gönderildi!')
            return redirect('ietisim')  # Kendi URL isminizi kullanın
        else:
            messages.error(request, 'Lütfen formu doğru şekilde doldurun.')
    else:
        form = ContactForm()

    return render(request, 'iletisim.html', {'form': form})



