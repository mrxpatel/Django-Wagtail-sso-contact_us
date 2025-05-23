# Generated by Django 5.1.8 on 2025-05-11 09:04

import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="contact_content",
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="contact_title",
            field=models.CharField(default="Get in Touch", max_length=255),
        ),
        migrations.AddField(
            model_name="homepage",
            name="featured_projects_content",
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="featured_projects_title",
            field=models.CharField(default="Featured Projects", max_length=255),
        ),
        migrations.AddField(
            model_name="homepage",
            name="skills_content",
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="skills_title",
            field=models.CharField(default="Skills", max_length=255),
        ),
    ]
