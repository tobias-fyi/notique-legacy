# Generated by Django 2.2.5 on 2019-10-05 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('logue', '0002_loguepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='loguepage',
            name='feed_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
