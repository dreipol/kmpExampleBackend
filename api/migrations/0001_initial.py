# Generated by Django 5.1.1 on 2024-09-25 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000, verbose_name='Content')),
                ('date_added', models.DateTimeField(auto_now=True, verbose_name='Date added')),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
    ]
