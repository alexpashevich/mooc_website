from django.contrib import admin
import moocs.models
# from moocs.models import Lesson

# class LessonAdmin(admin.ModelAdmin):
    # list_display = ('mooc', 'number', 'title')
    # list_filter = ('mooc',)

admin.site.register(moocs.models.Mooc)
admin.site.register(moocs.models.Lesson) #, LessonAdmin)
admin.site.register(moocs.models.Module)
admin.site.register(moocs.models.Lector)
admin.site.register(moocs.models.Language)
admin.site.register(moocs.models.University)