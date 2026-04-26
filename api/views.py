import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task, Note

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

@csrf_exempt
def note_detail_api(request, id):
    try:
        note = Note.objects.get(id=id)
    except Note.DoesNotExist:
        return JsonResponse({'error': 'Ghi chú không tồn tại.'}, status=404)

    # CHỖ TRỐNG CHO THÀNH VIÊN B (Lấy chi tiết - GET)
    if request.method == 'GET':
        return JsonResponse({
            'id': note.id,
            'title': note.title,
            'content': note.content,
            'created_at': note.created_at
        }, status=200)

    # CHỖ TRỐNG CHO THÀNH VIÊN B (Cập nhật - PUT/PATCH)
    elif request.method == 'PUT':
        # Thành viên B sẽ kéo code của bạn về và viết logic cập nhật vào đây
        pass

    elif request.method == 'DELETE':
        note.delete() # Lệnh xóa khỏi Database
        return JsonResponse({'message': 'Xóa ghi chú thành công.'}, status=200)

@csrf_exempt
def note_list_create(request):
    # Lấy danh sách toàn bộ Ghi chú
    if request.method == 'GET':
        notes = list(Note.objects.values('id', 'title', 'content', 'created_at'))
        return JsonResponse(notes, safe=False, status=200)

    # Tạo mới một Ghi chú 
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title', '').strip()
            content = data.get('content', '')

            # Kiểm tra dữ liệu đầu vào
            if not title:
                return JsonResponse({'error': 'Tiêu đề ghi chú không được để trống.'}, status=400)

            # Lưu vào Database
            new_note = Note.objects.create(title=title, content=content)
            
            return JsonResponse({
                'id': new_note.id,
                'title': new_note.title,
                'content': new_note.content,
                'created_at': new_note.created_at
            }, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Định dạng dữ liệu gửi lên không phải JSON.'}, status=400)