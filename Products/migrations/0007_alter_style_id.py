# Generated by Django 4.2.6 on 2023-11-01 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_alter_category_id_alter_subcategory_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
