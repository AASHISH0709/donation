# Generated by Django 3.2.5 on 2021-09-12 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_donation_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='email',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
