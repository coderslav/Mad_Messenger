# Generated by Django 3.2.6 on 2021-08-17 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_chatuser_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatuser',
            name='avatar',
            field=models.ImageField(default='static/chat/images/default_avatar.jpg', upload_to='static/chat/images/', verbose_name='Аватар'),
        ),
    ]