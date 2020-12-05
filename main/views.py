from django.shortcuts import render
from django.views import View

from main.models import News


class Layout(View):
    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'

    def get(self,request):
        news=News.objects.all()
        context={'title':'Новостная Страница',
                 'news':news
                 }
        return render(request,'main/index.html',context=context)
