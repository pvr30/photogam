# Generated by Django 3.2.8 on 2021-11-13 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_user_profile_pic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserFollowing',
        ),
    ]
