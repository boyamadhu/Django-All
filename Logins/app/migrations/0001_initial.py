# Generated by Django 4.1.7 on 2023-04-26 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('Password', models.IntegerField()),
                ('Re_EnterPassword', models.IntegerField()),
            ],
        ),
    ]
