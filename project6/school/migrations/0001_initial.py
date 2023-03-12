# Generated by Django 4.1.5 on 2023-03-02 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('School', models.CharField(max_length=100)),
                ('Sex', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Mjob', models.CharField(max_length=100)),
                ('Fjob', models.CharField(max_length=100)),
                ('Reason', models.CharField(max_length=100)),
                ('Guardian', models.CharField(max_length=100)),
                ('Paid', models.CharField(max_length=100)),
            ],
        ),
    ]