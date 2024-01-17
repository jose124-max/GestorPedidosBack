from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from Producto.models import Producto
from Combos.models import Combo
from .models import RecompensasProductos, RecompensasCombos

@method_decorator(csrf_exempt, name='dispatch')
class CrearRecompensaProducto(View):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            id_producto = request.POST.get('id_producto')
            puntos_recompensa_producto = request.POST.get('puntos_recompensa_producto')

            producto = Producto.objects.get(id_producto=id_producto)

            recompensa_producto = RecompensasProductos.objects.create(
                id_producto=producto,
                puntos_recompensa_producto=puntos_recompensa_producto,
                sestado=1
            )
            recompensa_producto.save()

            return JsonResponse({'mensaje': 'Recompensa de producto creada con éxito'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class CrearRecompensaCombo(View):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            id_combo = request.POST.get('id_combo')
            puntos_recompensa_combos = request.POST.get('puntos_recompensa_combos')

            combo = Combo.objects.get(id_combo=id_combo)

            recompensa_combo = RecompensasCombos.objects.create(
                id_combo=combo,
                puntos_recompensa_combos=puntos_recompensa_combos,
                sestado=1
            )
            recompensa_combo.save()

            return JsonResponse({'mensaje': 'Recompensa de combo creada con éxito'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
