# Generated by Django 5.0 on 2024-04-10 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_conformpassword_studentdetail_confirmpassword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetail',
            name='confirmpassword',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
