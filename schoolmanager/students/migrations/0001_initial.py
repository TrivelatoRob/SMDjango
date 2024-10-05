# Generated by Django 5.1.1 on 2024-10-05 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('matematica', 'Matemática'), ('portugues', 'Português'), ('historia', 'História'), ('geografia', 'Geografia'), ('ciencias', 'Ciências'), ('ingles', 'Inglês'), ('ed_fisica', 'Educação Física'), ('artes', 'Artes'), ('literatura', 'Literatura'), ('quimica', 'Química'), ('fisica', 'Física'), ('biologia', 'Biologia')], max_length=30)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('enrollment_date', models.DateField(auto_now_add=True)),
                ('courses', models.ManyToManyField(related_name='students', to='students.courses')),
            ],
        ),
    ]
