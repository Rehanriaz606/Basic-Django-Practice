# Generated by Django 4.0.3 on 2022-04-04 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pencil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.IntegerField(max_length=50)),
                ('p_name', models.CharField(max_length=100)),
                ('p_price', models.IntegerField(max_length=100)),
            ],
        ),
    ]
