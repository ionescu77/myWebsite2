# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("pub_date", models.DateTimeField()),
                ("text", models.TextField()),
                ("slug", models.SlugField(unique=True, max_length=40)),
            ],
            options={
                "ordering": ["-pub_date"],
            },
        ),
    ]
