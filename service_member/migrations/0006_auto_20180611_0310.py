# Generated by Django 2.0.5 on 2018-06-10 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_member', '0005_member_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='avatar',
            field=models.ImageField(default='default-img.png', upload_to=''),
        ),
    ]
