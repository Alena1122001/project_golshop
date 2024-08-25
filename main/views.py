from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories



class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Golshop - Главная'
        context['content'] = "Все для дома Golshop"
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Golshop - О нас'
        context['content'] = "О нас"
        context['text_on_page'] = "Мы дорожим нашей репутацией, поэтому разрабатываем свою продукцию самостоятельно и размещаем заказы на производство по всему миру, тщательно контролируя все производственные процессы. Мы предлагаем сбалансированы по цене, потребительским качествам и эстетике ассортимент, подходящийпод ваш текущий образ жизни. Будь то дом, квартира или дача, пикник на природе или отдых на море, вы всегда найдете у нас что-то, отвечающее вашим желаниям."
        return context
    
