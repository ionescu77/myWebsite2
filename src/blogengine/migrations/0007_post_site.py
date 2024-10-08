# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ("sites", "0001_initial"),
        ("blogengine", "0006_auto_20160621_1703"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="site",
            field=models.ForeignKey(
                default=1, to="sites.Site", on_delete=models.PROTECT
            ),
            preserve_default=False,
        ),
    ]
