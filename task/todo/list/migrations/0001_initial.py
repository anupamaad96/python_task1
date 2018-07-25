# Generated by Django 2.0.7 on 2018-07-25 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=400, null=True)),
                ('completion_date', models.DateTimeField()),
                ('priority', models.CharField(choices=[('high', 'High Priority'), ('highest', 'Highest priority'), ('low', 'Lowest priority')], max_length=100)),
                ('if_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
