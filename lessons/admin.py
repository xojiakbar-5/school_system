from django.contrib import admin
from .models import Lesson, ActionLog

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teacher', 'grade', 'day', 'start_time', 'end_time')
    list_filter = ('grade', 'day', 'teacher')
    search_fields = ('subject', 'teacher__username')

@admin.register(ActionLog)
class ActionLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user', 'action', 'subject')
    list_filter = ('action', 'user')
    search_fields = ('subject', 'user__username')
    readonly_fields = ('timestamp', 'user', 'action', 'subject')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
