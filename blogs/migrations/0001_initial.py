# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-27 20:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='AbstractCategoryMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AbstractPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('post_title', models.CharField(max_length=200)),
                ('post_content', models.TextField(blank=True)),
                ('featured_image', models.ImageField(blank=True, max_length=255, null=True, upload_to='images', verbose_name='Featured Image')),
                ('post_date', models.DateTimeField(verbose_name='Post Date')),
                ('post_excerpt', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['-post_date', 'post_title'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('abstractcategory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blogs.AbstractCategory')),
            ],
            options={
                'abstract': False,
            },
            bases=('blogs.abstractcategory',),
        ),
        migrations.CreateModel(
            name='CategoryMapping',
            fields=[
                ('abstractcategorymapping_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blogs.AbstractCategoryMapping')),
            ],
            options={
                'abstract': False,
            },
            bases=('blogs.abstractcategorymapping',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('abstractpost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blogs.AbstractPost')),
            ],
            options={
                'abstract': False,
            },
            bases=('blogs.abstractpost',),
        ),
        migrations.AddField(
            model_name='abstractpost',
            name='category',
            field=models.ManyToManyField(blank=True, through='blogs.AbstractCategoryMapping', to='blogs.AbstractCategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='abstractcategorymapping',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.AbstractCategory'),
        ),
        migrations.AddField(
            model_name='abstractcategorymapping',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.AbstractPost'),
        ),
    ]
