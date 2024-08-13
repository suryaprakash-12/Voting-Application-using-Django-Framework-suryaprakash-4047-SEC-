from django.contrib import admin

# Register your models here.

from .models import Question,Choice
# admin.site.register(Question)
# admin.site.register(Choice)

# class ChoiceInLine(admin.TabularInline):
#     model = Choice
#     extra = 3
class ChoiceInLines(admin.TabularInline):
    model = Choice
    extra = 4
 
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {
        'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInLines]


admin.site.register(Question, QuestionAdmin)
