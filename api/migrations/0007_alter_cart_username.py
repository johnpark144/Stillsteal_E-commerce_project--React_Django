# Generated by Django 4.1.3 on 2022-11-10 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_username_cart_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='username',
            field=models.TextField(),
        ),
    ]
