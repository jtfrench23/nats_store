# Generated by Django 2.2.4 on 2022-03-06 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.TextField()),
                ('product_type', models.CharField(max_length=45)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('size', models.CharField(max_length=10, null=True)),
                ('stock', models.IntegerField()),
                ('images', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
