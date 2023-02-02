#Django
from django.db import models


# Python
from typing import Any



class Stock(models.Model):
    """Stock model."""
    
    titile = models.CharField(
        max_length=50,
        verbose_name = "Название",
    )
    location = models.CharField(
        max_length = 100,
        verbose_name = "Местоположение"
    )
    number_of_handles = models.IntegerField(
        verbose_name='Количество ручек',
        default=0
    )
    
    class Meta:
        ordering = (
            "-titile",
        )
        verbose_name = "Склад"
        verbose_name_plural = "Склады"
        
    def __str__(self) -> str:
        return f"{self.titile} , {self.location}"


class Pen(models.Model):
    """Pen model."""
    
    MANUFACTURERS = [
        ("WE", "WENXUAN"), 
        ("AR", "Unkown")
    ]
    
    model_title = models.CharField(
        max_length = 100,
        verbose_name = "Название модели",
        unique=True,
        null=True
    )
    
    manufacturer = models.CharField(
        max_length=50,
        default=MANUFACTURERS[0][1],
        verbose_name = "Производитель",
        choices=MANUFACTURERS
    )
    
    stored = models.ManyToManyField(
        to = "Stock",
        verbose_name = 'Местоположение хранения'    
    )
    
    color = models.CharField(
        max_length = 50,
        verbose_name = 'цвет'
    )
    
    class Meta:
        ordering = (
            '-model_title',
        )
        verbose_name = 'Ручка'
        verbose_name_plural = 'Ручки'
        
    def save(
        self,
        *args,
        **kwargs
        ):
        # self.full_clean()
        # self.activation_code = utils.generate_model_name()
        return super().save(*args, **kwargs)
    