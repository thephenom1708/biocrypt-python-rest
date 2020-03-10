# Generated by Django 3.0.2 on 2020-03-10 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0002_auto_20200310_0408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='share',
            name='user_id',
        ),
        migrations.CreateModel(
            name='UserShareMapping',
            fields=[
                ('user_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('shares', models.ManyToManyField(blank=True, null=True, to='apitest.Share')),
            ],
        ),
    ]
