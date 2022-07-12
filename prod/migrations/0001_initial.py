# Generated by Django 4.0.4 on 2022-07-05 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.CharField(max_length=8, null=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('img', models.ImageField(upload_to='images')),
            ],
        ),
    ]
