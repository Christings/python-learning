# Generated by Django 2.2.7 on 2019-11-06 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('type', '0002_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='category_type',
            field=models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目'), (4, '四级类目')], default='1', help_text='类别描述', verbose_name='类别描述'),
        ),
    ]