# Generated by Django 4.2.11 on 2024-04-07 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_homepage_rtf_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='rtf_text',
        ),
    ]
