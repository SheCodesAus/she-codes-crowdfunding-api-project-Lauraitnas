# Generated by Django 4.0.2 on 2022-04-25 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_remove_association_association_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='association',
            name='association_name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
