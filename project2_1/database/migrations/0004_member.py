# Generated by Django 3.2.3 on 2021-06-03 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
