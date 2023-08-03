# Generated by Django 4.2.3 on 2023-08-03 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InfluencerList', '0002_media_fix_media_info_users_fix_users_info_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media_fix',
            name='id',
        ),
        migrations.RemoveField(
            model_name='users_fix',
            name='id',
        ),
        migrations.AlterField(
            model_name='media_fix',
            name='media_id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='media_info',
            name='comments_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='media_info',
            name='like_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='media_info',
            name='media_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InfluencerList.media_fix'),
        ),
        migrations.AlterField(
            model_name='users_fix',
            name='ig_id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='users_info',
            name='ig_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InfluencerList.users_fix'),
        ),
        migrations.AlterModelTable(
            name='media_fix',
            table='Media_fix',
        ),
        migrations.AlterModelTable(
            name='media_info',
            table='Media_info',
        ),
        migrations.AlterModelTable(
            name='users_fix',
            table='Users_fix',
        ),
        migrations.AlterModelTable(
            name='users_info',
            table='Users_info',
        ),
    ]
