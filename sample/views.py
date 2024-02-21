from django.shortcuts import render
from sample.models import Sample
# Create your views here.


def index(request):

    context = dict()  # Boş bir context sözlüğü oluşturuldu

    # Tüm Sample objelerini alın ve 'samples' adlı bir anahtarla context'e eklendi
    context['samples'] = Sample.objects.all() #SELECT * FROM sample

    # 'index.html' şablonunu kullanarak HTTP yanıtını render edin ve döndürün
    return render(request, 'index.html', context)

