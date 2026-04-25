import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task

def health_check(request):
    return JsonResponse({"status": "ok"})

@csrf_exempt
def task_list_create(request):
    if request.method == 'GET':
        tasks = list(Task.objects.values('id', 'title', 'is_done'))
        return JsonResponse(tasks, safe=False, status=200)

    elif request.method == 'POST':
        try:
            body = json.loads(request.body)
            title = body.get('title', '').strip()

            if not title:
                return JsonResponse({'error': 'Vui lòng cung cấp title.'}, status=400)

            new_task = Task.objects.create(title=title)
            return JsonResponse({
                'id': new_task.id,
                'title': new_task.title,
                'is_done': new_task.is_done
            }, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON không hợp lệ.'}, status=400)