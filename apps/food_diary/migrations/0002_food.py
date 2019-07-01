# Generated by Django 2.1.10 on 2019-07-01 10:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_diary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('calories', models.IntegerField(help_text='Calories per 100g', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(900)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='food_diary.FoodCategory')),
            ],
        ),
    ]
