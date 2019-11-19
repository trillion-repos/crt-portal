# Generated by Django 2.2.4 on 2019-11-13 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0014_auto_20191108_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='status',
            field=models.TextField(choices=[('new', 'New'), ('open', 'Open'), ('closed', 'Closed')], default='new'),
        ),
        migrations.AlterField(
            model_name='protectedclass',
            name='protected_class',
            field=models.CharField(blank=True, choices=[('disability', 'Disability (including temporary or recovery)'), ('race', 'Race/color'), ('origin', 'National origin (including ancestry, ethnicity, and language)'), ('immigration', 'Immigration/citizenship status (choosing this will not share your status)'), ('religion', 'Religion'), ('gender', 'Sex or gender identity (including gender stereotypes) or pregnancy'), ('orientation', 'Sexual orientation'), ('family', 'Family, marriage, or parental status'), ('military', 'Military status'), ('age', 'Age'), ('genetic', 'Genetic information'), ('other', 'Other reason')], max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='primary_complaint',
            field=models.CharField(choices=[('workplace', 'Workplace discrimination or other employment-related problem'), ('housing', 'Housing discrimination or harassment'), ('education', 'Discrimination at a school, educational program, or related to receiving education'), ('voting', 'Right to vote impacted'), ('police', 'Mistreated by police, law enforcement, or correctional staff (including while in prison)'), ('commercial_or_public', 'Discriminated against in any other commercial location or public place'), ('something_else', 'Something else happened')], default='', max_length=100),
        ),
    ]