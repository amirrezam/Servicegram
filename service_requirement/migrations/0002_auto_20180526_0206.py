# Generated by Django 2.0.5 on 2018-05-25 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_member', '0003_auto_20180526_0156'),
        ('service_requirement', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NonHelpCash',
            new_name='HelpNonCash',
        ),
    ]
