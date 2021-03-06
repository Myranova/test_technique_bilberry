# Generated by Django 2.0.7 on 2018-08-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_contactphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='')),
                ('timestamp', models.CharField(max_length=100)),
                ('verified_flag', models.BooleanField()),
                ('rejected_flag', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='ContactPhoto',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
