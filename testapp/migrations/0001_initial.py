# Generated by Django 2.1.1 on 2019-04-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empno', models.IntegerField()),
                ('empname', models.CharField(max_length=60)),
                ('empadd', models.CharField(max_length=60)),
                ('empsal', models.FloatField()),
            ],
        ),
    ]
