# Generated by Django 4.1.4 on 2023-01-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_alter_person_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='idea_image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
