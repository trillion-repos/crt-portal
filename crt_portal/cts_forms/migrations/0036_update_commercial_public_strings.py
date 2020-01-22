# Generated by Django 2.2.8 on 2020-01-22 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0035_add_commercial_public_location_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='commercial_or_public_place',
            field=models.CharField(choices=[('place_of_worship', 'Place of worship or about a place of worship'), ('store', 'Commercial or retail building'), ('healthcare', 'Healthcare facility'), ('financial', 'Financial institution'), ('public_space', 'Public space'), ('other', 'Other')], default=None, max_length=225, null=True),
        ),
    ]