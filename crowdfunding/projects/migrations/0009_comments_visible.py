# Generated by Django 4.0.2 on 2022-03-28 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_remove_pledge_comment_delete_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
