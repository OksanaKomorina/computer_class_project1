# Generated by Django 5.0.6 on 2024-08-05 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer_class_app', '0005_alter_progessrecordbook_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('FeedbackID', models.AutoField(primary_key=True, serialize=False)),
                ('Feedback', models.TextField()),
                ('ParticipateID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computer_class_app.participants')),
            ],
        ),
    ]
