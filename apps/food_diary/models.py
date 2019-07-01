from datetime import datetime
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models


class FoodCategory(models.Model):
    name = models.CharField(
        max_length=100)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name


class Portion(models.Model):
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    SNACK = "snack"

    food = models.ForeignKey(
        Food,
        on_delete=models.PROTECT,
    )
    amount = models.PositiveIntegerField()
    day = models.DateField(
        blank=True,
        default=datetime.now,
    )
    meal = models.TextField(
        choices=(
            (BREAKFAST, "breakfast"),
            (LUNCH, "lunch"),
            (DINNER, "dinner"),
            (SNACK, "snack")
        ),
        default=SNACK,
    )

    def __str__(self):
        return f" {self.amount}g {self.food}"
