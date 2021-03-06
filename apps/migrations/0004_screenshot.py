# Generated by Django 4.0.4 on 2022-04-27 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apps', '0003_app_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScreenShot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenshot', models.ImageField(upload_to='media')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.app')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'app')},
            },
        ),
    ]
