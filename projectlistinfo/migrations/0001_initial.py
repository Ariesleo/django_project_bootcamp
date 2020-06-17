# Generated by Django 3.0.7 on 2020-06-14 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectListInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('project_name', models.CharField(max_length=50)),
                ('proj_demo_link', models.CharField(max_length=250)),
                ('proj_source_link', models.CharField(max_length=250)),
                ('tools_used', models.CharField(max_length=250)),
                ('remarks', models.TextField()),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]