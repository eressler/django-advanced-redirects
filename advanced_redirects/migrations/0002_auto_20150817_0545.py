# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advanced_redirects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='redirect',
            options={'ordering': ('originating_url',), 'verbose_name': 'redirect', 'verbose_name_plural': 'redirects'},
        ),
        migrations.AlterField(
            model_name='redirect',
            name='id',
            field=models.CharField(max_length=129, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='redirect',
            name='originating_url',
            field=models.CharField(help_text=b'The originating URL that triggered a 404 error or is manually entered.', max_length=255),
        ),
    ]
