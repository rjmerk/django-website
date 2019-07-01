from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models


class FoodCategory(models.Model):
    name = models.CharField(
        max_length=100)


class Food(models.Model):
    name = models.CharField(
        max_length=100)
    calories = models.IntegerField(
        validators=[
            MinValueValidator(1),
            # 9 calories/g fat, maximum calories possible for food
            MaxValueValidator(900)
        ],
        help_text="Calories per 100g"
    )
    category = models.ForeignKey(
        FoodCategory,
        on_delete=models.PROTECT,
    )
