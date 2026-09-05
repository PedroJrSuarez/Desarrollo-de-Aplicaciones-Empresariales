from django.http import JsonResponse
from django.shortcuts import render

from .models import Item


def item_list(request):
    items = Item.objects.order_by('-created_at')
    return render(request, 'core/item_list.html', {'items': items})


def item_api(request):
    items = list(Item.objects.order_by('-created_at').values('id', 'name', 'description', 'created_at'))
    for item in items:
        item['created_at'] = item['created_at'].isoformat() if item['created_at'] else None
    return JsonResponse(items, safe=False)
