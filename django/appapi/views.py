from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import RasPi

from django.http.response import HttpResponse
from .forms import RasPiForm
import random
from django.shortcuts import redirect

# 個別IDの桁数
INDIVIDUAL_ID_LENGTH = 5

def index(request):
    """
    ラズパイ一覧画面
    """
    raspi = RasPi.objects.all()

    return render(request, 'management/raspi/index.html', {
        'raspis': raspi
    })

def create(request):
    """
    ラズパイ登録画面
    """
    # form作成
    form = RasPiForm()
    return render(request, 'management/raspi/create.html', {
        'form': form,
    })

def store(request):
    """
    ラズパイ登録処理
    """

    # individual_id 生成
    judge = False
    while(judge == False):
        individual_id = create_individual_id()
        if not RasPi.objects.filter(individual_id = individual_id).exists():
            judge = True

    # RasPi データ作成
    raspi = RasPi(
        individual_id = individual_id,
        mac_address = request.POST['mac_address'],
        in_use = request.POST['in_use'],
    )
    raspi.save()

    return redirect('raspi_index')

def create_individual_id():
    """
    個別ID生成処理
    """
    digit = INDIVIDUAL_ID_LENGTH # 桁数
    individual_id = random.randrange(10**(digit-1),10**digit)
    return individual_id
