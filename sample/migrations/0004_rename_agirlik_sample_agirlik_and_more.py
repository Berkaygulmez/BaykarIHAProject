# Generated by Django 5.0.2 on 2024-02-20 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0003_rename_price_sample_agirlik_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='Agirlik',
            new_name='agirlik',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='Kategori',
            new_name='kategori',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='Marka',
            new_name='marka',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='Model',
            new_name='model',
        ),
    ]
