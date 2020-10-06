# Generated by Django 2.2.13 on 2020-09-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_OrderBundles'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=32, unique=True, verbose_name='Promo Code')),
                ('discount_percent', models.IntegerField(verbose_name='Discount percent')),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Promo Code',
                'verbose_name_plural': 'Promo Codes',
            },
        ),
    ]