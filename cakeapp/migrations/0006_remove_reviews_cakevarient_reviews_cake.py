# Generated by Django 4.2.7 on 2023-11-13 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='cakevarient',
        ),
        migrations.AddField(
            model_name='reviews',
            name='cake',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cakeapp.cakes'),
        ),
    ]