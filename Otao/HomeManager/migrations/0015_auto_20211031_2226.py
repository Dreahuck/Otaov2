# Generated by Django 2.2.24 on 2021-10-31 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeManager', '0014_auto_20211023_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='tchouCoinWallet',
            field=models.DecimalField(decimal_places=9, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='tache',
            name='tchouCoin',
            field=models.DecimalField(decimal_places=9, default=0, max_digits=10),
        ),
    ]