# Generated by Django 3.2 on 2021-06-20 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('overview', models.TextField()),
                ('thumbnail', models.ImageField(default='no_image.jpeg', upload_to='post')),
                ('view_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.author')),
                ('categories', models.ManyToManyField(to='blogapp.Category')),
            ],
        ),
    ]
