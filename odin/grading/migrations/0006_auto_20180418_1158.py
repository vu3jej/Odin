# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-18 11:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grading', '0005_graderplainproblemwithrequirements'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GraderBinaryProblem',
        ),
        migrations.DeleteModel(
            name='GraderPlainProblem',
        ),
        migrations.DeleteModel(
            name='GraderPlainProblemWithRequirements',
        ),
    ]
