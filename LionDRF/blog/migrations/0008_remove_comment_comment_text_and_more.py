# Generated by Django 5.0.3 on 2024-05-30 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_comment_comment_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_text',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
    ]