# Generated by Django 5.0.6 on 2024-06-03 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_author_alter_article_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='Məzmun'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Başlıq'),
        ),
    ]
