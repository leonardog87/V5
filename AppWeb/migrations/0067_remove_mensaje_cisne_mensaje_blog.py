# Generated by Django 4.2.3 on 2023-09-09 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0066_mensaje_delete_blogmensaje'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensaje',
            name='cisne',
        ),
        migrations.AddField(
            model_name='mensaje',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mensajes', to='AppWeb.blog'),
        ),
    ]