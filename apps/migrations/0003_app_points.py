# Generated by Django 4.0.4 on 2022-04-27 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_remove_subcategory_category_app_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='points',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
