# Generated by Django 4.1.2 on 2024-10-14 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_tarea_fechamax'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='prioridad',
            field=models.IntegerField(choices=[(1, 'Baja'), (3, 'Media'), (5, 'Alta')], default=1, null=True),
        ),
    ]