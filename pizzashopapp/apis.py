from django.http import JsonResponse

from .models import PizzaShop, Pizza
from pizzashopapp.serializers import PizzaShopSerializer, PizzaSerializer


def client_get_pizzashops(request):
    pizzashop = PizzaShopSerializer(
        PizzaShop.objects.all().order_by('-id'),
        many=True,
        context={'request': request}
    ).data

    return JsonResponse({'pizzashops': pizzashop})


def client_get_pizzas(request, pizzashop_id):
    pizzas = PizzaSerializer(
        Pizza.objects.filter(pizzashop_id=pizzashop_id).order_by('-id'),
        many=True,
        context={'request': request}
    ).data

    return JsonResponse({'pizzas': pizzas})
