# Generated by Django 3.2.8 on 2021-11-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_alter_post_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]