# Generated by Django 4.0.2 on 2022-03-26 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_comments_date_posted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pledge',
            name='comment',
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]