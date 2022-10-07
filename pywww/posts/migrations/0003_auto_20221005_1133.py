# Generated by Django 3.2.15 on 2022-10-05 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('posts', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='example_file',
            field=models.FileField(blank=True, null=True, upload_to='posts/examples/'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='tags.Tag'),
        ),
    ]
