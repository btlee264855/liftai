# Generated by Django 4.1.3 on 2022-11-13 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_exercise_delete_members_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('link', models.TextField()),
            ],
        ),
    ]
