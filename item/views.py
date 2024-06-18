from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Item


def detail(request, pk):

    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return render(request, 'core/404.html')
    return render(request, 'item/detail.html', {
        'item' : item
    })

    # ideia tela erro 404
    # item = get_object_or_404(Item, pk=pk)

