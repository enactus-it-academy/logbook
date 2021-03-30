from django.db import models


class Feedback(models.Model):
    name = models.CharField('Имя', max_length=150, blank=True)
    image = models.ImageField('Изображение', upload_to="feedbacks/%Y/%m", blank=True)
    phone_number = models.CharField('Номер телефона', max_length=50, blank=True)
    email = models.EmailField('Электронная почта', blank=True)
    message = models.TextField('Подробнее')
    date = models.DateTimeField('Дата обращения', auto_now_add=True)
