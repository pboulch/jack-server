# Generated by Django 3.2.8 on 2022-04-01 12:31

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('api', '0009_room_refresh_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('friendly_name', models.CharField(max_length=50)),
                ('access_code', models.CharField(max_length=200, unique=True)),
                ('spotify_token', models.CharField(max_length=200)),
                ('refresh_token', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='userroom',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='UserRoom',
        ),
    ]
