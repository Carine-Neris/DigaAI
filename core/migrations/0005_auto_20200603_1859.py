# Generated by Django 3.0.4 on 2020-06-03 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200603_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='nome',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
