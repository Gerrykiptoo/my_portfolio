# Generated by Django 5.0.7 on 2024-08-20 22:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_contactmessage_project_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HireMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('project_description', models.TextField()),
                ('budget', models.CharField(max_length=50)),
                ('timeline', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='message',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='title',
        ),
        migrations.RemoveField(
            model_name='techskill',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='techskill',
            name='name',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='message',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='name',
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
