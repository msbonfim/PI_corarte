from django.shortcuts import render
from django.http import HttpResponse
from galeria.models import Imagem

# Create your views here.
def home(request):
    return render(request, 'index.html')

def index(request):
    imagens = Imagem.objects.all().order_by('-criado_em')  # pega as imagens
    return render(request, 'home/index.html', {'imagens': imagens})
    
