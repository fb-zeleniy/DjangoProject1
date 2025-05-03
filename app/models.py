from django.contrib.auth.models import User
from django.db import models
from django.core.validators import *
import re




class Kinds(models.TextChoices):
    Buy = 'b', 'Куплю'
    Sell = 's', 'Продам'
    Change = 'c', 'Обмен'

class Rubric(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return f"/app/rubric/{self.pk}/"


def validate_even(value):
    if value % 2 == 0:
        raise ValidationError(f"Число чётное")

class MinMaxValueValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self,value):
        if value < self.min_value or value >= self.max_value:
            raise ValidationError("Ваша цена вышла за диапазон")




class Bb(models.Model):
    rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Товар", validators=[RegexValidator("^.{4,}$")])
    price = models.FloatField(blank=True,null=True, verbose_name="Цена", )
    content = models.TextField(blank=True,null=True, verbose_name="Описание")
    published=models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    result = Bb.objects.aggreagate(
        min_price = min("price"),
        max_price = max('price')
    )



    # for bb in Bb.objects.all():
    #     if f"({bb.id})" not in bb.title:
    #         bb.title = f"{bb.title} ({bb.id})"
    #         bb.save()
    #
    #
    # for bb in Bb.objects.all():
    #     # Находим все цифры в заголовке
    #     digits = re.findall(r'\d', bb.title)
    #
    #     if any(int(d) % 2 == 1 for d in digits):
    #         bb.delete()
    #
    #
    #
    # if f"({bb.id})" not in bb.title:
    #     bb.title = f"{bb.title} ({bb.id})"
    #     bb.save()

    def get_absolute_url(self):
        return f"/app/bb/{self.pk}/"
    def save(self, *args, **kwargs):
        if self.title=="Оружие":
            return ValidationError
        super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        if self.title=="Мяч":
            return ValidationError('Нельзя')
        super().delete(*args, **kwargs)


    def title_and_price(self):

        if self.price:
            return  f"Title: {self.title}, Price: {self.price}$"
        else:
            return f"Title: {self.title}$"


    def content(self):
        if self.content:
            return f"Content: {self.title}$"

    def published(self):
        if self.published:
            return f" Published: {self.published}$"


   def my_new_validatitaor(self, value):
        if value <0:
            raise ValidationError("Число не может быть меньше нуля")
        else:
            print("Всё ок")

# KINDS =(
#     ('Куплю-продам',
#         ('b', 'Куплю'),
#         ('s', 'Продам'),
# ),
#     ('Обмен'
#     ('c', 'Обменяю'),)
# )

# kinds = models.CharField(max_length=1, default='s', choices=KINDS)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Объявления"
        verbose_name = "Объявления"
        ordering = ["-published"]
        # constraints = (
        #     models.CheckConstraint(
        #         check=models.Q(price__gt=0) & models.Q(price__lte=100),
        #         name = 'board_price_check',
        #     )
        # )

class Passport(models.Model):
    country=models.CharField(max_length=100)
    user=models.OneToOneField(User, on_delete=models.CASCADE)


class Spare(models.Model):
    name = models.CharField(max_length=30)

class Machine(models.Model):
    name = models.CharField(max_length=30)
    spares = models.ManyToManyField(Spare)

# class Human(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#
#     def __str__(self):
#         return self.name
#
# class Child(Human):
#     flavor = models.CharField(max_length=150)
#
#     def __str__(self):
#         return f"{self.name} (Имя ребёнка)"
#
#
# class IceCream(models.Model):
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     flavor = models.CharField(max_length=150)
#
#     def __str__(self):
#         return self.flavor, self.price
#
# # class IceCreamShop( models.Model):
#     location = models.CharField(max_length=150)
#     ice_creams = models.ManyToManyField(IceCream)
#     owner = models.ForeignKey(Human, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"Киоск расположен на {self.location}"