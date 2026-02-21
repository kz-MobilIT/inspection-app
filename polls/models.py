from django.db import models
from django.core.validators import MinValueValidator

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    car_model = models.CharField(max_length=100, blank=True)
    mileage = models.IntegerField(default=0, validators=[MinValueValidator(0)])

