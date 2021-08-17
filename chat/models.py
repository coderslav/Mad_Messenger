from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ChatUser(models.Model):
    SEX_TYPES = (('M', 'Мужчина'), ('W', 'Женщина'), ('N', 'Неопределенный'))
    chat_user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(verbose_name='Возраст')
    sex = models.CharField(max_length=50, choices=SEX_TYPES, default='N', verbose_name='Пол')
    avatar = models.ImageField(upload_to='static/chat/images/', default='static/chat/images/default_avatar.jpg',
                               verbose_name='Аватар')
    joined_at = models.DateTimeField(auto_now_add=True, verbose_name='Время регистрации')

    def __str__(self):
        return self.chat_user.username

    class Meta:
        verbose_name = 'Пользователь чата'
        verbose_name_plural = 'Пользователи чата'


class Room (models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название комнаты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Message (models.Model):
    author = models.ForeignKey(ChatUser, on_delete=models.CASCADE)
    body = models.TextField(blank=True, verbose_name='Сообщение')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Время отправки сообщения')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author}: {self.body[:15]}...'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
