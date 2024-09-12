# Generated by Django 4.2 on 2024-09-12 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizador',
            name='email',
            field=models.EmailField(default='prueba@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='evento',
            name='organizador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to='eventos.organizador'),
        ),
    ]
