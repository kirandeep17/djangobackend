# Generated by Django 4.2.3 on 2023-08-03 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0009_remove_user_state_alter_user_address_line_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
