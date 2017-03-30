# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_aocops_indexbulletin'),
    ]

    operations = [
        migrations.AddField(
            model_name='aocops_indexbulletin',
            name='Bull_name',
            field=models.CharField(max_length=20, null=True, verbose_name='\u516c\u544a\u6807\u9898'),
        ),
    ]
