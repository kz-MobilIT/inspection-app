from django.contrib import admin
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "car_model", "mileage", "pub_date")
    search_fields = ("question_text", "car_model")
    list_filter = ("car_model", "pub_date")
    ordering = ("-pub_date",)





