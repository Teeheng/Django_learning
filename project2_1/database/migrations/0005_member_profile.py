# Generated by Django 3.2.3 on 2021-06-03 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='profile',
            field=models.ImageField(default='profile/user.png', upload_to='profile/'),
        ),
    ]
