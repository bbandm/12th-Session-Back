# Generated by Django 5.0.3 on 2024-05-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_hashtag_post_hashtag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='blog_photo')),
                ('hashtag', models.ManyToManyField(to='blog.hashtag')),
            ],
        ),
    ]
