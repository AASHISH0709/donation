# Generated by Django 3.2.5 on 2021-09-12 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_donation_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='email',
        ),
    ]
