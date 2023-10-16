# Generated by Django 4.2.5 on 2023-10-10 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_avaliacao_da_cozinha_descricao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cozinha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=9000)),
                ('foto', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='avaliacao_da_cozinha',
            name='id_da_cozinha',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='cozinha', to='core.cozinha'),
            preserve_default=False,
        ),
    ]