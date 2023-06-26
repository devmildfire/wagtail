# Generated by Django 4.2.2 on 2023-06-25 14:00

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='rtfbody',
            field=wagtail.fields.RichTextField(blank=True, null=True, verbose_name='Расширенное текстовое поле'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Подзаголовок'),
        ),
    ]
