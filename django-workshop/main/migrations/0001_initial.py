# Generated by Django 5.1.3 on 2024-11-08 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('turma', models.CharField(max_length=100)),
                ('aprovado', models.BooleanField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
