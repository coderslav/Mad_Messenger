from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    REQUIRED_FIELDS = ['email', 'age']
    SEX_CHOICES = (('M', 'Мужчина'), ('W', 'Женщина'), ('N', 'Неопределенный'))
    age = models.IntegerField(verbose_name='Возраст')
    sex = models.CharField(max_length=50, choices=SEX_CHOICES, default='N', verbose_name='Пол')
    avatar = models.ImageField(upload_to='static/chat/images/', default='static/chat/images/default_avatar.png',
                               verbose_name='Аватар')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь чата'
        verbose_name_plural = 'Пользователи чата'


class Room (models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название комнаты')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время отправки создания комнаты')
    participants = models.ManyToManyField(User, blank=True, verbose_name='Юзеры комнаты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Message (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True, verbose_name='Сообщение')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время отправки сообщения')
    time = models.CharField(max_length=10, default='00:00:00', verbose_name='Локальное время отправки')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Чат комната')
    count_in_room = models.CharField(max_length=255, verbose_name='Уникальный идентификатор')
    is_private = models.BooleanField(default=False, verbose_name='Является ли сообщение приватным')

    def __str__(self):
        return f'{self.author}: {self.body[:15]}...'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('date',)
