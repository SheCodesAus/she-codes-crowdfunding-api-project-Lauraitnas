# Generated by Django 4.0.2 on 2022-03-22 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_category_project_deadline_alter_project_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='categories',
        ),
        migrations.AddField(
            model_name='project',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='projects.category'),
        ),
    ]
