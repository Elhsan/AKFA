from django.shortcuts import render
from .forms import OrderForms
from .models import Order
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    order = Order.objects.all()
    return render(request, 'news/news_home.html', {'order':order})


class NewsDetailView(DetailView):
    model = Order
    template_name = 'news/detail_view.html'
    context_object_name = 'order'
    pk_url_kwarg = 'pk'

class NewsUpdatView(UpdateView):
    model = Order
    template_name = 'news/create_order.html'
    context_object_name = 'order'
    pk_url_kwarg = 'pk'
    fields = ('имя','размеры','стоимость','материал',)

class NewsDeleteView(DeleteView):
    model = Order
    success_url = '/news/'
    template_name = 'news/delete_order.html'



def create_order(request):
    if request.method == 'POST':
        form = OrderForms(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            error = "э ты че ввел исправил быстро"
    error = ''
    form = OrderForms()

    date = {
        'form': form,
        'error': error
    }

    return render(request, "news/create_order.html", date)
