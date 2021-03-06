# Generated by Django 3.1.5 on 2021-01-25 22:32

import address.models
import autoslug.fields
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import properties.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('address', '0003_auto_20200830_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=True, null=True, populate_from=properties.models.get_slug, unique=True)),
                ('property_name', models.CharField(blank=True, max_length=255, null=True)),
                ('features', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, help_text='Key features for this property', size=None, verbose_name='Key Features')),
                ('description', models.TextField()),
                ('available_from', models.DateField(blank=True, default=None, null=True)),
                ('building_size', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('availability', models.IntegerField(blank=True, null=True)),
                ('images', models.FileField(blank=True, null=True, upload_to='properties/images')),
                ('address', address.models.AddressField(on_delete=django.db.models.deletion.CASCADE, to='address.address')),
                ('owner', models.ForeignKey(help_text="Property's owner.", on_delete=django.db.models.deletion.CASCADE, related_name='properties', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_on',),
            },
        ),
    ]
