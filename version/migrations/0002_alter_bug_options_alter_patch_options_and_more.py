# Generated by Django 5.1.3 on 2024-11-10 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bug',
            options={'verbose_name': 'Bug', 'verbose_name_plural': 'Bugs'},
        ),
        migrations.AlterModelOptions(
            name='patch',
            options={'verbose_name': 'Patch', 'verbose_name_plural': 'Patches'},
        ),
        migrations.AlterModelOptions(
            name='platform',
            options={'verbose_name': 'Platform', 'verbose_name_plural': 'Platforms'},
        ),
        migrations.AlterModelOptions(
            name='test',
            options={'verbose_name': 'Test', 'verbose_name_plural': 'Tests'},
        ),
        migrations.AlterField(
            model_name='bug',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='version.platform', verbose_name='Platform'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='patch',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='patch',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='patch',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='version.platform', verbose_name='Platform'),
        ),
        migrations.AlterField(
            model_name='patch',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='patch',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='status',
            field=models.CharField(choices=[('PreAlpha', 'PreAlpha'), ('Alpha', 'Alpha'), ('Beta', 'Beta'), ('Gamma', 'Gamma'), ('RC', 'RC'), ('Rolling', 'Rolling'), ('Stable', 'Stable')], max_length=10, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='url',
            field=models.URLField(verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='version',
            field=models.BigIntegerField(verbose_name='Version'),
        ),
        migrations.AlterField(
            model_name='test',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='test',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='test',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='version.platform', verbose_name='Platform'),
        ),
        migrations.AlterField(
            model_name='test',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='test',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
    ]
