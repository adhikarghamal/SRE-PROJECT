# Generated by Django 5.1.3 on 2024-11-30 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('question', models.TextField()),
                ('response1', models.TextField()),
                ('response2', models.TextField()),
            ],
        ),
    ]
