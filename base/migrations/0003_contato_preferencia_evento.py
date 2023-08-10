# Generated by Django 3.2.12 on 2023-08-10 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_contato_modificado_em'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='preferencia_evento',
            field=models.CharField(choices=[('todos', 'Todos'), ('musicais', 'Eventos Musicais'), ('esportivos', 'Eventos Esportivos'), ('educativos', 'Eventos Educativos')], default='todos', max_length=50, verbose_name='Preferência de Evento'),
        ),
    ]
