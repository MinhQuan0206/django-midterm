# Django Midterm (Backend) — Hướng dẫn cho người B (Ngày 2–3)

Tài liệu này phục vụ đúng nhiệm vụ **thành viên B (ngày 2–3)**:

- **Bài 2**: Tạo model `Task`, migrate, cấu hình `admin.py`, tạo 3 bản ghi mẫu (Admin).
- **Lý thuyết**: tóm tắt **Models** và **Views (FBV vs CBV)** để đưa vào slide/báo cáo.

## Yêu cầu

- Python 3.x
- (Khuyến khích) Windows PowerShell

## Cài đặt & chạy dự án (Windows)

Mở terminal tại thư mục `django-midterm/`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Sau đó truy cập:

- Admin: `http://127.0.0.1:8000/admin/`

## Tạo tài khoản Admin

```powershell
python manage.py createsuperuser
```

Đăng nhập tại trang admin rồi tạo dữ liệu mẫu.

## Bài 2 — Model `Task` + migrate + tạo 3 bản ghi mẫu (Admin)

### Model

- `Task(title: string, is_done: boolean)`
  - `title`: required
  - `is_done`: default `false`

### Migrate DB

Nếu bạn mới clone về hoặc xóa DB cũ:

```powershell
python manage.py migrate
```

### Tạo 3 bản ghi mẫu bằng Admin

1. Vào `http://127.0.0.1:8000/admin/`
2. Đăng nhập
3. Chọn **Tasks** → **Add**
4. Tạo 3 bản ghi, ví dụ:
   - `Học Django` / `is_done=false`
   - `Làm bài GK` / `is_done=false`
   - `Test API tasks` / `is_done=true`

## Gợi ý nội dung slide/báo cáo (Lý thuyết)

### Models (Django ORM)

- Model là lớp Python ánh xạ thành bảng trong DB; mỗi field là một cột.
- Migrations giúp versioning schema DB:
  - `python manage.py makemigrations` tạo file migration
  - `python manage.py migrate` áp migration lên DB
- Admin site giúp CRUD nhanh, tiện tạo dữ liệu mẫu.

### Views (FBV vs CBV)

- View xử lý request và trả response (ở bài này trả JSON).
- FBV: dễ đọc, phù hợp bài nhỏ; thường dùng `if request.method == ...`.
- CBV: tái sử dụng tốt cho CRUD lớn (mixins), nhưng “trừu tượng” hơn.

