import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Note

# Tạo 2 note mẫu
note1 = Note.objects.create(
    title='Học Django',
    content='Làm slide và báo cáo'
)
note2 = Note.objects.create(
    title='API Design',
    content='Thiết kế RESTful API'
)

print(f"Đã tạo {Note.objects.count()} notes:")
for note in Note.objects.all():
    print(f"  - {note.id}: {note.title}")
