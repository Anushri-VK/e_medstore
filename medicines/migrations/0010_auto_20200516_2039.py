# Generated by Django 3.0.5 on 2020-05-16 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicines', '0009_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineOrdered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Combiflam', models.IntegerField(default=0)),
                ('Paracetamol', models.IntegerField(default=0)),
                ('Cofsils', models.IntegerField(default=0)),
                ('DigeneTablet', models.IntegerField(default=0)),
                ('DigeneGel', models.IntegerField(default=0)),
                ('Hajmola', models.IntegerField(default=0)),
                ('Seacod', models.IntegerField(default=0)),
                ('Shelcal', models.IntegerField(default=0)),
                ('Crocin', models.IntegerField(default=0)),
                ('Lubrifresh', models.IntegerField(default=0)),
                ('Dettol', models.IntegerField(default=0)),
                ('Ashwagandha', models.IntegerField(default=0)),
                ('Moov', models.IntegerField(default=0)),
                ('Zandu', models.IntegerField(default=0)),
                ('Vicks', models.IntegerField(default=0)),
                ('Chyawanprash', models.IntegerField(default=0)),
                ('totalSum', models.BigIntegerField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Medicines',
        ),
    ]
