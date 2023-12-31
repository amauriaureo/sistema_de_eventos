# Generated by Django 3.2.12 on 2023-08-16 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['nome'], 'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('descricao', models.TextField(blank=True, verbose_name='Descricao')),
                ('data', models.DateField(blank=True, null=True, verbose_name='Data do Evento')),
                ('publicado', models.BooleanField(default=False, verbose_name='Publicado')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.categoria')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
    ]
