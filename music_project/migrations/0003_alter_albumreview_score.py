# Generated by Django 5.1.4 on 2024-12-14 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_project', '0002_alter_albumreview_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumreview',
            name='score',
            field=models.IntegerField(choices=[('1', '1 out of 10'), ('2', '2 out of 10'), ('3', '3 out of 10'), ('4', '4 out of 10'), ('5', '5 out of 10'), ('6', '6 out of 10'), ('7', '7 out of 10'), ('8', '8 out of 10'), ('9', '9 out of 10'), ('10', '10 out of 10')]),
        ),
    ]