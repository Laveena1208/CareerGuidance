# Generated by Django 3.2.8 on 2022-01-31 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_after10_question_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='username',
        ),
        migrations.AddField(
            model_name='result',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='result',
            name='question_type',
            field=models.CharField(default='', max_length=50),
        ),
    ]
