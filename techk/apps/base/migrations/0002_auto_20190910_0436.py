# Generated by Django 2.0.5 on 2019-09-10 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
