# Generated by Django 4.2.5 on 2023-10-10 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_cozinha_avaliacao_da_cozinha_id_da_cozinha'),
    ]

    operations = [
        migrations.AddField(
            model_name='cozinha',
            name='nome',
            field=models.CharField(default='trapezaria', max_length=500),
            preserve_default=False,
        ),
    ]
