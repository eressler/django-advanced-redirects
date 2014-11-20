# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Redirect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('originating_url', models.CharField(help_text=b'The originating URL that triggered a 404 error or is manually entered.', unique=True, max_length=1000)),
                ('redirect_to_url', models.CharField(help_text=b'Optional. Specify the URL to which the originating URL should redirect. This should be an absolute or root-relative URL.', max_length=1000, null=True, blank=True)),
                ('redirect_type', models.CharField(default=b'301', max_length=10, choices=[(b'301', b'301 - Permanent'), (b'302', b'302 - Temporary')])),
            ],
            options={
                'ordering': ('originating_url',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referer_url', models.CharField(help_text=b'The URL of the previous page that redirected to this url that generated the 404 error.', max_length=1000)),
                ('hits', models.PositiveIntegerField(default=0, help_text=b'The number of times the originating URL has been hit.')),
                ('last_hit', models.DateTimeField(help_text=b'The last time the originating URL was hit.', null=True, blank=True)),
                ('redirect', models.ForeignKey(related_name='referrals', to='advanced_redirects.Redirect')),
            ],
            options={
                'ordering': ('-hits',),
            },
            bases=(models.Model,),
        ),
    ]
