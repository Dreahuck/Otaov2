# Generated by Django 3.0.8 on 2021-08-30 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeManager', '0003_auto_20210828_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='commentaire_text',
            field=models.CharField(max_length=6000),
        ),
        migrations.AlterField(
            model_name='tache',
            name='jalon_date',
            field=models.DateTimeField(null=True, verbose_name='Date Jalon de réalisation'),
        ),
        migrations.AlterField(
            model_name='tache',
            name='priseEnChargePar_id',
            field=models.IntegerField(default=-1),
        ),
    ]
