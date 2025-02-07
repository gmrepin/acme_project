from django.contrib import admin

from .models import Birthday


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
    )
    list_display_links = ('first_name', 'last_name',)
    # Разрешаю редактирование для удобства тестирования.
