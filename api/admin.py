from django.contrib import admin

from .models import Task, Note


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_done")
    list_filter = ("is_done",)
    search_fields = ("title",)
    ordering = ("-id",)

# Đăng ký hiển thị cho Note (Nhiệm vụ của A nhưng bạn làm hộ)
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title", "content")
    ordering = ("-created_at",)
