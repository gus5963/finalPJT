# Generated by Django 3.2.5 on 2022-02-28 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BbsList',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('writer', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=500)),
                ('regdate', models.DateTimeField(auto_now=True)),
                ('viewcnt', models.IntegerField(default=0)),
            ],
        ),
    ]