# Generated by Django 4.2.5 on 2023-09-28 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_rename_no_of_items_library_no_of_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='library/images/'),
        ),
    ]
