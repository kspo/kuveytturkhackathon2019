# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-14 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='buyOrSell',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='market',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='paymentType',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='senderSuffix',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='submitted',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='balanceTr',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='balanceUsd',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='iban',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]
