# Generated by Django 4.1.4 on 2023-01-04 21:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0011_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='point',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(5)]),
            preserve_default=False,
        ),
    ]