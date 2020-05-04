# Generated by Django 3.0.5 on 2020-05-02 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApiRest', '0002_ingrediente_hamburguesa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingrediente',
            name='hamburguesa',
        ),
        migrations.AddField(
            model_name='hamburguesa',
            name='ingrediente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ingredientes', to='ApiRest.Ingrediente'),
            preserve_default=False,
        ),
    ]
