# Generated by Django 3.1.4 on 2020-12-06 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0004_auto_20201206_1034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='locationexpire',
            options={'ordering': ['order']},
        ),
        migrations.AlterUniqueTogether(
            name='locationexpire',
            unique_together={('track', 'order')},
        ),
    ]
