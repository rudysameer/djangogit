# Generated by Django 4.2.4 on 2023-09-12 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('used_for', models.CharField(max_length=200)),
                ('row_1', models.CharField(max_length=200)),
                ('row_2', models.CharField(max_length=200)),
                ('row_3', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
