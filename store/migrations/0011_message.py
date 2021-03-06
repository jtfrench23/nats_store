# Generated by Django 2.2.4 on 2022-03-22 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_remove_customer_birth_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=500)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Customer')),
            ],
        ),
    ]
