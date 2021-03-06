# Generated by Django 4.0.2 on 2022-03-22 11:42

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('association_number', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='social',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
