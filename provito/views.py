from django.shortcuts import render
from .models import Board, Category
from django.views import generic


def index(request):
    board = Board.objects.all()
    category = Category.objects.all()
    return render(request, 'provito/index.html', {'board': board, 'category': category})


class BoardList(generic.ListView):
    model = Board
    template_name = 'provito/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['board'] = Board.objects.all()
        context['category'] = Category.objects.all()
        return context