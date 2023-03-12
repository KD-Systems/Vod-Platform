# Generated by Django 4.1.7 on 2023-03-12 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0002_channel_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='business_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='channel',
            name='business_location',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='channel',
            name='facebook',
            field=models.URLField(default='https://facebook.com/'),
        ),
        migrations.AddField(
            model_name='channel',
            name='instagram',
            field=models.URLField(default='https://instagram.com/'),
        ),
        migrations.AddField(
            model_name='channel',
            name='make_business_email_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='channel',
            name='make_business_location_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='channel',
            name='total_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='channel',
            name='twitter',
            field=models.URLField(default='https://twitter.com/'),
        ),
        migrations.AddField(
            model_name='channel',
            name='website',
            field=models.URLField(default='https://my-website.com/'),
        ),
    ]