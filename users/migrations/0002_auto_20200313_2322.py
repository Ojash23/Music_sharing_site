# Generated by Django 3.0.3 on 2020-03-13 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('username', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='friend',
            name='followee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='users.User'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followees', to='users.User'),
        ),
    ]
