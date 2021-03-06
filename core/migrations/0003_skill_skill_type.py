# Generated by Django 3.2.8 on 2021-10-27 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20211028_0216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('icon', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('skill', models.ManyToManyField(related_name='skill', to='core.Skill')),
            ],
        ),
    ]
