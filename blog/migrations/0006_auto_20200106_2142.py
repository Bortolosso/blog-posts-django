# Generated by Django 3.0.1 on 2020-01-06 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_userprofileinfo_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='nick_name',
            field=models.CharField(default=None, max_length=12, unique=True),
        ),
    ]
