# Generated by Django 4.2.6 on 2023-10-23 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_remove_style_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='style_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
