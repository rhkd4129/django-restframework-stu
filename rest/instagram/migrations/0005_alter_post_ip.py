# Generated by Django 4.0.3 on 2022-03-25 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instagram", "0004_post_ip"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="ip",
            field=models.GenericIPAddressField(editable=False, null=True),
        ),
    ]
