# Generated by Django 3.2.6 on 2021-08-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Generated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255, verbose_name='URL')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Generated',
                'verbose_name_plural': "Generated's",
            },
        ),
    ]