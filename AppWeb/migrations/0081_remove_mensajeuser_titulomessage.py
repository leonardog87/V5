# Generated by Django 4.2.3 on 2023-10-07 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0080_rename_user_receiver_mensajeuser_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensajeuser',
            name='titulomessage',
        ),
    ]
