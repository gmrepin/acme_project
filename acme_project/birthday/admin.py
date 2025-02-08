from django.contrib import admin

from .models import Birthday, Tag


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
    )
    list_display_links = ('first_name', 'last_name',)
    # Разрешаю редактирование для удобства тестирования.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass