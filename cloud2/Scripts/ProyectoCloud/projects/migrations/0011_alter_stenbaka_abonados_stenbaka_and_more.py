# Generated by Django 4.2.13 on 2024-05-25 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_stenbaka_abonados_stenbaka_ingresos_stenbaka_trafico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stenbaka_abonados',
            name='stenbaka',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stenbaka_ingresos',
            name='stenbaka',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stenbaka_trafico',
            name='stenbaka',
            field=models.SmallIntegerField(null=True),
        ),
    ]
