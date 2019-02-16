# Generated by Django 2.1.7 on 2019-02-16 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='broker',
            name='email',
            field=models.CharField(default='broker@email.com', max_length=100),
        ),
        migrations.AddField(
            model_name='broker',
            name='password',
            field=models.CharField(default='password', max_length=100),
        ),
        migrations.AddField(
            model_name='broker',
            name='passwordconfirmation',
            field=models.CharField(default='passwordconfirmation', max_length=100),
        ),
        migrations.AlterField(
            model_name='broker',
            name='name',
            field=models.CharField(default='broker', max_length=100),
        ),
    ]
