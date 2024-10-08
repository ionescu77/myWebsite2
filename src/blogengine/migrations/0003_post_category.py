# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blogengine", "0002_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                blank=True,
                to="blogengine.Category",
                null=True,
                on_delete=models.SET_NULL,
            ),
        ),
    ]
