# Generated by Django 3.0.5 on 2020-05-16 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0006_auto_20200512_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=300)),
            ],
        ),
    ]
