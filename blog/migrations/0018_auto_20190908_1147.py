# Generated by Django 2.2.5 on 2019-09-08 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20190908_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='draft', max_length=10),
        ),
    ]
