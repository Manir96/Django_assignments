# Generated by Django 4.2.4 on 2023-08-26 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=300)),
                ('Last_Name', models.CharField(max_length=300)),
                ('Email', models.EmailField(max_length=300)),
                ('phone_number', models.CharField(max_length=12)),
                ('batch', models.IntegerField()),
                ('texarea', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=40)),
                ('re_password', models.CharField(max_length=40)),
                ('checkbox', models.CharField(max_length=50)),
                ('payment', models.DecimalField(decimal_places=2, max_digits=6)),
                ('django', models.BooleanField(max_length=30)),
            ],
        ),
    ]