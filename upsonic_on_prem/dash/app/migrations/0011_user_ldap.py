# Generated by Django 4.2.9 on 2024-08-18 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0010_ai_task_ai_output_ai_task_user_input"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="ldap",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
