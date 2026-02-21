from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/edit/", views.edit, name="edit"),
    path("<int:question_id>/delete/", views.delete, name="delete"),

]
