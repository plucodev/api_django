# Generated by Django 2.1.1 on 2019-01-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_contact_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='agenda_slug',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
